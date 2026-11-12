import json
import secrets
from datetime import datetime, timezone
from uuid import UUID

from fastapi import HTTPException, status
from redis import Redis
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import User
from app.schemas.user import InternalVerifyResponse, NonceResponse, UserProfile
from app.services.siwe import SiweValidationError, parse_and_verify_siwe_message
from app.services.telegram_auth import TelegramIdentity

_NONCE_KEY_PREFIX = "auth:nonce:"
_LINK_WALLET_NONCE_KEY_PREFIX = "auth:link-wallet:nonce:"
_SESSION_KEY_PREFIX = "auth:session:"
_CONSUME_NONCE_SCRIPT = """
local nonce = redis.call('GET', KEYS[1])
if nonce == ARGV[1] then
    return redis.call('DEL', KEYS[1])
end
return 0
"""


def _nonce_key(wallet_address: str) -> str:
    return f"{_NONCE_KEY_PREFIX}{wallet_address.lower()}"


def _link_wallet_nonce_key(user_id: UUID, wallet_address: str) -> str:
    return f"{_LINK_WALLET_NONCE_KEY_PREFIX}{user_id}:{wallet_address.lower()}"


def _session_key(session_id: str) -> str:
    return f"{_SESSION_KEY_PREFIX}{session_id}"


def _create_session(user: User, cache: Redis) -> InternalVerifyResponse:
    session_id = secrets.token_urlsafe(32)
    session_data = json.dumps(
        {
            "user_id": str(user.id),
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        separators=(",", ":"),
    )
    cache.set(
        _session_key(session_id),
        session_data,
        ex=settings.session_ttl_seconds,
    )
    return InternalVerifyResponse(
        user=UserProfile.model_validate(user),
        expires_in=settings.session_ttl_seconds,
        session_id=session_id,
    )


def issue_nonce(wallet_address: str, cache: Redis) -> NonceResponse:
    nonce = secrets.token_hex(16)
    cache.set(
        _nonce_key(wallet_address),
        nonce,
        ex=settings.nonce_ttl_seconds,
    )
    return NonceResponse(nonce=nonce, expires_in=settings.nonce_ttl_seconds)


def _consume_nonce(wallet_address: str, nonce: str, cache: Redis) -> None:
    consumed = cache.eval(
        _CONSUME_NONCE_SCRIPT,
        1,
        _nonce_key(wallet_address),
        nonce,
    )
    if consumed != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nonce is invalid, expired, or already used",
        )


def _get_or_create_user(wallet_address: str, db: Session) -> User:
    user = db.scalar(select(User).where(User.wallet_address == wallet_address))
    if user is None:
        user = User(wallet_address=wallet_address)
        db.add(user)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            user = db.scalar(
                select(User).where(User.wallet_address == wallet_address)
            )
            if user is None:
                raise
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )
    return user


def verify_wallet(
    message: str,
    signature: str,
    db: Session,
    cache: Redis,
) -> InternalVerifyResponse:
    try:
        siwe_message = parse_and_verify_siwe_message(message, signature)
    except SiweValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc

    _consume_nonce(siwe_message.address, siwe_message.nonce, cache)
    user = _get_or_create_user(siwe_message.address, db)
    return _create_session(user, cache)


def _resolve_referrer(start_param: str | None, db: Session) -> User | None:
    if start_param is None:
        return None
    if not start_param.startswith("ref_"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Telegram referral parameter",
        )
    try:
        referrer_id = UUID(start_param.removeprefix("ref_"))
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Telegram referral parameter",
        ) from exc
    referrer = db.get(User, referrer_id)
    if referrer is None or not referrer.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Telegram referrer was not found or is inactive",
        )
    return referrer


def authenticate_telegram(
    identity: TelegramIdentity,
    db: Session,
    cache: Redis,
) -> InternalVerifyResponse:
    user = db.scalar(select(User).where(User.telegram_id == identity.telegram_id))
    if user is None:
        referrer = _resolve_referrer(identity.start_param, db)
        user = User(
            telegram_id=identity.telegram_id,
            telegram_username=identity.telegram_username,
            first_name=identity.first_name,
            avatar_url=identity.avatar_url,
            referrer_id=referrer.id if referrer is not None else None,
        )
        db.add(user)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            user = db.scalar(
                select(User).where(User.telegram_id == identity.telegram_id)
            )
            if user is None:
                raise
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )
    user.telegram_username = identity.telegram_username
    user.first_name = identity.first_name
    user.avatar_url = identity.avatar_url
    db.commit()
    db.refresh(user)
    return _create_session(user, cache)


def issue_link_wallet_nonce(
    user: User,
    wallet_address: str,
    cache: Redis,
) -> NonceResponse:
    if user.telegram_id is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wallet linking requires a Telegram-linked account",
        )
    nonce = secrets.token_hex(16)
    cache.set(
        _link_wallet_nonce_key(user.id, wallet_address),
        nonce,
        ex=settings.nonce_ttl_seconds,
    )
    return NonceResponse(nonce=nonce, expires_in=settings.nonce_ttl_seconds)


def _consume_link_wallet_nonce(
    user: User,
    wallet_address: str,
    nonce: str,
    cache: Redis,
) -> None:
    consumed = cache.eval(
        _CONSUME_NONCE_SCRIPT,
        1,
        _link_wallet_nonce_key(user.id, wallet_address),
        nonce,
    )
    if consumed != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wallet-link nonce is invalid, expired, or already used",
        )


def link_wallet(
    user: User,
    message: str,
    signature: str,
    db: Session,
    cache: Redis,
) -> UserProfile:
    if user.telegram_id is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wallet linking requires a Telegram-linked account",
        )
    try:
        siwe_message = parse_and_verify_siwe_message(message, signature)
    except SiweValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc
    _consume_link_wallet_nonce(user, siwe_message.address, siwe_message.nonce, cache)

    locked_user = db.scalar(select(User).where(User.id == user.id).with_for_update())
    if locked_user is None or not locked_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is invalid or the account is inactive",
        )
    if locked_user.wallet_address is not None:
        if locked_user.wallet_address == siwe_message.address:
            return UserProfile.model_validate(locked_user)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A different wallet is already linked to this account",
        )
    wallet_owner = db.scalar(
        select(User).where(User.wallet_address == siwe_message.address)
    )
    if wallet_owner is not None and wallet_owner.id != locked_user.id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Wallet is already linked to another account",
        )

    locked_user.wallet_address = siwe_message.address
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Wallet is already linked to another account",
        ) from exc
    db.refresh(locked_user)
    return UserProfile.model_validate(locked_user)


def get_current_user(session_id: str, db: Session, cache: Redis) -> User:
    session_data = cache.get(_session_key(session_id))
    if session_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is invalid or expired",
        )
    try:
        user_id = UUID(json.loads(session_data)["user_id"])
    except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        cache.delete(_session_key(session_id))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is invalid",
        ) from exc

    user = db.get(User, user_id)
    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is invalid or the account is inactive",
        )
    return user


def logout(session_id: str | None, cache: Redis) -> None:
    if session_id:
        cache.delete(_session_key(session_id))
