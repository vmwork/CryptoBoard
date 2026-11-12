import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qsl, urlencode

import pytest
from eth_account import Account
from eth_account.messages import encode_defunct

os.environ.setdefault(
    "TELEGRAM_BOT_TOKEN",
    "8823138444:AAFNwE-5GSUxd5ZEY65V7ygsMC_errQ_k74",
)
os.environ.setdefault("TELEGRAM_BOT_USERNAME", "CryptoBoard_Dev_bot")

from app.core.config import settings
from app.models.user import User
from app.services import auth_service
from app.services.telegram_auth import (
    TelegramAuthError,
    TelegramIdentity,
    validate_webapp_init_data,
    validate_widget_payload,
)


TELEGRAM_TOKEN = settings.telegram_bot_token


def _render_webapp_init_data(
    user_data: dict[str, object],
    auth_date: int,
    *,
    start_param: str | None = None,
) -> str:
    payload = {
        "auth_date": str(auth_date),
        "user": json.dumps(user_data, separators=(",", ":"), ensure_ascii=False),
    }
    if start_param is not None:
        payload["start_param"] = start_param
    data_check_string = "\n".join(
        f"{key}={value}" for key, value in sorted(payload.items())
    )
    secret_key = hmac.new(
        b"WebAppData",
        TELEGRAM_TOKEN.encode(),
        hashlib.sha256,
    ).digest()
    payload["hash"] = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256,
    ).hexdigest()
    return urlencode(payload)


def _render_widget_payload(auth_date: int) -> dict[str, object]:
    payload = {
        "id": 31337,
        "first_name": "Dev",
        "last_name": "Tester",
        "username": "cw_dev",
        "photo_url": "https://example.com/avatar.png",
        "auth_date": auth_date,
    }
    if any(isinstance(value, (dict, list, tuple, bool)) for value in payload.values()):
        raise AssertionError("Test payload must only contain scalars")
    data_check_string = "\n".join(
        f"{key}={value}" for key, value in sorted(payload.items())
    )
    secret_key = hashlib.sha256(TELEGRAM_TOKEN.encode()).digest()
    payload["hash"] = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256,
    ).hexdigest()
    return payload


def _create_signed_siwe_message(nonce: str, address: str, private_key: str | bytes) -> tuple[str, str]:
    issued_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    message = (
        f"{settings.siwe_domain} wants you to sign in with your Ethereum account:\n"
        f"{address}\n\n"
        f"URI: {settings.siwe_uri}\n"
        "Version: 1\n"
        f"Chain ID: {settings.evm_chain_id}\n"
        f"Nonce: {nonce}\n"
        f"Issued At: {issued_at}"
    )
    signature = Account.sign_message(
        encode_defunct(text=message),
        private_key=private_key,
    ).signature.hex()
    return message, signature


def test_validate_webapp_init_data_accepts_valid_payload() -> None:
    now = datetime.now(timezone.utc)
    auth_date = int(now.timestamp())
    user_data = {
        "id": 1,
        "first_name": "Dev",
        "username": "classifyd_bot",
        "photo_url": "https://example.com/avatar.png",
    }
    payload = _render_webapp_init_data(
        user_data,
        auth_date,
        start_param="ref_01234567-89ab-cdef-0123-456789abcdef",
    )
    identity = validate_webapp_init_data(payload, now=now)
    assert identity.telegram_id == user_data["id"]
    assert identity.start_param == "ref_01234567-89ab-cdef-0123-456789abcdef"


def test_validate_webapp_init_data_rejects_bad_signature() -> None:
    now = datetime.now(timezone.utc)
    auth_date = int(now.timestamp())
    user_data = {
        "id": 2,
        "first_name": "Dev",
        "username": "classifyd_bot",
    }
    original_payload = _render_webapp_init_data(user_data, auth_date)
    parsed = dict(parse_qsl(original_payload))
    parsed["hash"] = "0" * 64
    tampered = urlencode(parsed)
    with pytest.raises(TelegramAuthError):
        validate_webapp_init_data(tampered, now=now)


def test_validate_webapp_init_data_rejects_expired_date() -> None:
    now = datetime.now(timezone.utc)
    auth_date = int((now - timedelta(minutes=20)).timestamp())
    user_data = {
        "id": 3,
        "first_name": "Dev",
        "username": "classifyd_bot",
    }
    payload = _render_webapp_init_data(user_data, auth_date)
    with pytest.raises(TelegramAuthError):
        validate_webapp_init_data(payload, now=now)


def test_validate_widget_payload_accepts_valid_data() -> None:
    now = datetime.now(timezone.utc)
    auth_date = int(now.timestamp())
    payload = _render_widget_payload(auth_date)
    identity = validate_widget_payload(payload, now=now)
    assert identity.telegram_id == payload["id"]
    assert identity.telegram_username == payload["username"]


def test_validate_widget_payload_rejects_bad_signature() -> None:
    now = datetime.now(timezone.utc)
    auth_date = int(now.timestamp())
    payload = _render_widget_payload(auth_date)
    payload_with_bad_hash = payload.copy()
    payload_with_bad_hash["hash"] = "0" * 64
    with pytest.raises(TelegramAuthError):
        validate_widget_payload(payload_with_bad_hash, now=now)


def test_authenticate_telegram_assigns_referrer_and_creates_session(
    sqlite_session,
    fake_cache,
) -> None:
    referrer = User(telegram_id=99, first_name="Referrer")
    sqlite_session.add(referrer)
    sqlite_session.commit()
    identity = TelegramIdentity(
        telegram_id=123,
        telegram_username="referred",
        first_name="Referred",
        avatar_url="https://example.com/avatar.png",
        start_param=f"ref_{referrer.id}",
    )
    result = auth_service.authenticate_telegram(identity, sqlite_session, fake_cache)
    assert result.user.telegram_id == identity.telegram_id
    assert result.user.referrer_id == referrer.id
    session_key = auth_service._session_key(result.session_id)
    assert session_key in fake_cache.data


def test_link_wallet_consumes_nonce_and_sets_wallet(
    sqlite_session,
    fake_cache,
) -> None:
    user = User(telegram_id=321, first_name="LinkUser")
    sqlite_session.add(user)
    sqlite_session.commit()
    session_user = sqlite_session.get(User, user.id)
    assert session_user is not None
    account = Account.create()
    wallet_address = account.address
    wallet_message = auth_service.issue_link_wallet_nonce(
        session_user,
        wallet_address,
        fake_cache,
    )
    message, signature = _create_signed_siwe_message(
        wallet_message.nonce,
        wallet_address,
        account.key,
    )
    result = auth_service.link_wallet(
        session_user,
        message,
        signature,
        sqlite_session,
        fake_cache,
    )
    assert result.wallet_address == wallet_address.lower()
    link_key = auth_service._link_wallet_nonce_key(session_user.id, wallet_address)
    assert link_key not in fake_cache.data
