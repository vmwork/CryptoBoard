from typing import Annotated

from fastapi import APIRouter, Cookie, HTTPException, status

from app.api.dependencies import Cache, CurrentUser, DbSession
from app.core.config import settings
from app.core.security import sign_session_id, unsign_session_id
from app.schemas.user import (
    InternalVerifyResponse,
    LinkWalletRequest,
    LogoutResponse,
    NonceRequest,
    NonceResponse,
    TelegramWebAppRequest,
    TelegramWidgetRequest,
    UserProfile,
    VerifyRequest,
)
from app.services import auth_service
from app.services.telegram_auth import (
    TelegramAuthError,
    validate_webapp_init_data,
    validate_widget_payload,
)

router = APIRouter(prefix="/auth", tags=["auth"])

SessionCookie = Annotated[
    str | None,
    Cookie(alias=settings.session_cookie_name),
]


@router.post("/nonce", response_model=NonceResponse)
def request_nonce(payload: NonceRequest, cache: Cache) -> NonceResponse:
    return auth_service.issue_nonce(payload.wallet_address, cache)


@router.post("/verify", response_model=InternalVerifyResponse)
def verify_signature(
    payload: VerifyRequest,
    db: DbSession,
    cache: Cache,
) -> InternalVerifyResponse:
    result = auth_service.verify_wallet(
        payload.message,
        payload.signature,
        db,
        cache,
    )
    return InternalVerifyResponse(
        user=result.user,
        expires_in=result.expires_in,
        session_id=sign_session_id(result.session_id),
    )


def _telegram_auth_error(error: TelegramAuthError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"code": "TELEGRAM_AUTH_INVALID", "message": str(error)},
    )


@router.post("/telegram/webapp", response_model=InternalVerifyResponse)
def telegram_webapp(
    payload: TelegramWebAppRequest,
    db: DbSession,
    cache: Cache,
) -> InternalVerifyResponse:
    try:
        identity = validate_webapp_init_data(payload.init_data)
    except TelegramAuthError as error:
        raise _telegram_auth_error(error) from error
    result = auth_service.authenticate_telegram(identity, db, cache)
    result.session_id = sign_session_id(result.session_id)
    return result


@router.post("/telegram/widget", response_model=InternalVerifyResponse)
def telegram_widget(
    payload: TelegramWidgetRequest,
    db: DbSession,
    cache: Cache,
) -> InternalVerifyResponse:
    try:
        identity = validate_widget_payload(payload.model_dump(exclude_none=True))
    except TelegramAuthError as error:
        raise _telegram_auth_error(error) from error
    result = auth_service.authenticate_telegram(identity, db, cache)
    result.session_id = sign_session_id(result.session_id)
    return result


@router.post("/link-wallet/nonce", response_model=NonceResponse)
def link_wallet_nonce(
    payload: NonceRequest,
    current_user: CurrentUser,
    cache: Cache,
) -> NonceResponse:
    return auth_service.issue_link_wallet_nonce(
        current_user, payload.wallet_address, cache
    )


@router.post("/link-wallet", response_model=UserProfile)
def link_wallet(
    payload: LinkWalletRequest,
    current_user: CurrentUser,
    db: DbSession,
    cache: Cache,
) -> UserProfile:
    return auth_service.link_wallet(
        current_user, payload.message, payload.signature, db, cache
    )


@router.get("/me", response_model=UserProfile)
def read_current_user(
    db: DbSession,
    cache: Cache,
    session_cookie: SessionCookie = None,
) -> UserProfile:
    session_id = unsign_session_id(session_cookie)
    if session_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session cookie is missing or invalid",
        )
    return UserProfile.model_validate(
        auth_service.get_current_user(session_id, db, cache)
    )


@router.post("/logout", response_model=LogoutResponse)
def logout_session(
    cache: Cache,
    session_cookie: SessionCookie = None,
) -> LogoutResponse:
    auth_service.logout(unsign_session_id(session_cookie), cache)
    return LogoutResponse(success=True)
