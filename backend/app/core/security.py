import base64
import hashlib
import hmac
from typing import Annotated

from fastapi import Header, HTTPException, status

from app.core.config import settings


def require_internal_bff_secret(
    x_internal_bff_secret: Annotated[str | None, Header()] = None,
) -> None:
    expected = settings.internal_bff_secret.encode()
    provided = (x_internal_bff_secret or "").encode()
    if not hmac.compare_digest(provided, expected):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid internal BFF credentials",
        )


def sign_session_id(session_id: str) -> str:
    signature = hmac.new(
        settings.secret_key.encode(),
        session_id.encode(),
        hashlib.sha256,
    ).digest()
    encoded = base64.urlsafe_b64encode(signature).rstrip(b"=").decode()
    return f"{session_id}.{encoded}"


def unsign_session_id(value: str | None) -> str | None:
    if not value or value.count(".") != 1:
        return None
    session_id, provided_signature = value.split(".", 1)
    if not session_id or not provided_signature:
        return None
    expected_signature = sign_session_id(session_id).split(".", 1)[1]
    if not hmac.compare_digest(provided_signature, expected_signature):
        return None
    return session_id
