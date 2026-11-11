from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from redis import Redis
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import sign_session_id, unsign_session_id
from app.db.cache import get_redis_client
from app.db.session import get_db
from app.schemas.user import (
    InternalVerifyResponse,
    LogoutResponse,
    NonceRequest,
    NonceResponse,
    UserProfile,
    VerifyRequest,
)
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

DbSession = Annotated[Session, Depends(get_db)]
Cache = Annotated[Redis, Depends(get_redis_client)]
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
