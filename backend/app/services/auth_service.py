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

_NONCE_KEY_PREFIX = "auth:nonce:"
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


def _session_key(session_id: str) -> str:
    return f"{_SESSION_KEY_PREFIX}{session_id}"


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
