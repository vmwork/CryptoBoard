from typing import Annotated

from fastapi import Cookie, Depends, HTTPException, status
from redis import Redis
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import unsign_session_id
from app.db.cache import get_redis_client
from app.db.session import get_db
from app.models.user import User
from app.services import auth_service

DbSession = Annotated[Session, Depends(get_db)]
Cache = Annotated[Redis, Depends(get_redis_client)]
SessionCookie = Annotated[str | None, Cookie(alias=settings.session_cookie_name)]


def get_optional_current_user(
    db: DbSession,
    cache: Cache,
    session_cookie: SessionCookie = None,
) -> User | None:
    session_id = unsign_session_id(session_cookie)
    if session_id is None:
        if session_cookie:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session cookie is missing or invalid",
            )
        return None
    return auth_service.get_current_user(session_id, db, cache)


def get_current_user(
    user: Annotated[User | None, Depends(get_optional_current_user)],
) -> User:
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication is required",
        )
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
OptionalCurrentUser = Annotated[User | None, Depends(get_optional_current_user)]
