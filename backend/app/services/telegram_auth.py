import hashlib
import hmac
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Mapping
from urllib.parse import parse_qsl

from app.core.config import settings

TELEGRAM_AUTH_MAX_AGE_SECONDS = 15 * 60


class TelegramAuthError(ValueError):
    pass


@dataclass(frozen=True)
class TelegramIdentity:
    telegram_id: int
    telegram_username: str | None
    first_name: str
    avatar_url: str | None
    start_param: str | None = None


def _current_timestamp(now: datetime | None) -> int:
    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)
    return int(current_time.timestamp())


def _validate_auth_date(auth_date: object, now: datetime | None) -> None:
    if isinstance(auth_date, bool):
        raise TelegramAuthError("Invalid Telegram auth date")
    try:
        timestamp = int(auth_date)
    except (TypeError, ValueError) as exc:
        raise TelegramAuthError("Invalid Telegram auth date") from exc
    if str(auth_date).strip() != str(timestamp) or timestamp <= 0:
        raise TelegramAuthError("Invalid Telegram auth date")

    current_timestamp = _current_timestamp(now)
    if timestamp > current_timestamp:
        raise TelegramAuthError("Telegram auth date is in the future")
    if current_timestamp - timestamp > TELEGRAM_AUTH_MAX_AGE_SECONDS:
        raise TelegramAuthError("Telegram authentication has expired")


def _validate_hash(received_hash: object, expected_hash: str) -> None:
    if not isinstance(received_hash, str) or len(received_hash) != 64:
        raise TelegramAuthError("Invalid Telegram hash")
    try:
        bytes.fromhex(received_hash)
    except ValueError as exc:
        raise TelegramAuthError("Invalid Telegram hash") from exc
    if not hmac.compare_digest(received_hash.lower(), expected_hash):
        raise TelegramAuthError("Invalid Telegram signature")


def _identity_from_user(
    user: object,
    *,
    start_param: str | None = None,
) -> TelegramIdentity:
    if not isinstance(user, dict):
        raise TelegramAuthError("Invalid Telegram user data")
    telegram_id = user.get("id")
    first_name = user.get("first_name")
    username = user.get("username")
    photo_url = user.get("photo_url")
    if (
        isinstance(telegram_id, bool)
        or not isinstance(telegram_id, int)
        or telegram_id <= 0
    ):
        raise TelegramAuthError("Invalid Telegram user ID")
    if not isinstance(first_name, str) or not first_name.strip():
        raise TelegramAuthError("Invalid Telegram first name")
    if len(first_name) > 64:
        raise TelegramAuthError("Telegram first name is too long")
    if username is not None and (
        not isinstance(username, str) or len(username) > 32
    ):
        raise TelegramAuthError("Invalid Telegram username")
    if photo_url is not None and (
        not isinstance(photo_url, str) or len(photo_url) > 2048
    ):
        raise TelegramAuthError("Invalid Telegram photo URL")
    return TelegramIdentity(
        telegram_id=telegram_id,
        telegram_username=username,
        first_name=first_name,
        avatar_url=photo_url,
        start_param=start_param,
    )


def validate_webapp_init_data(
    init_data: str,
    *,
    bot_token: str | None = None,
    now: datetime | None = None,
) -> TelegramIdentity:
    try:
        pairs = parse_qsl(
            init_data,
            keep_blank_values=True,
            strict_parsing=True,
            max_num_fields=100,
        )
    except ValueError as exc:
        raise TelegramAuthError("Invalid Telegram init data") from exc
    if not pairs or len({key for key, _ in pairs}) != len(pairs):
        raise TelegramAuthError("Invalid Telegram init data")

    data = dict(pairs)
    received_hash = data.pop("hash", None)
    if received_hash is None or "auth_date" not in data or "user" not in data:
        raise TelegramAuthError("Incomplete Telegram init data")
    data_check_string = "\n".join(
        f"{key}={value}" for key, value in sorted(data.items())
    )
    token = bot_token if bot_token is not None else settings.telegram_bot_token
    if not token:
        raise TelegramAuthError("Telegram bot token is not configured")
    secret_key = hmac.new(
        b"WebAppData",
        token.encode(),
        hashlib.sha256,
    ).digest()
    expected_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256,
    ).hexdigest()
    _validate_hash(received_hash, expected_hash)
    _validate_auth_date(data["auth_date"], now)

    try:
        user = json.loads(data["user"])
    except (TypeError, json.JSONDecodeError) as exc:
        raise TelegramAuthError("Invalid Telegram user data") from exc
    start_param = data.get("start_param")
    if start_param is not None and len(start_param) > 64:
        raise TelegramAuthError("Invalid Telegram start parameter")
    return _identity_from_user(user, start_param=start_param)


def validate_widget_payload(
    payload: Mapping[str, object],
    *,
    bot_token: str | None = None,
    now: datetime | None = None,
) -> TelegramIdentity:
    data = dict(payload)
    received_hash = data.pop("hash", None)
    if received_hash is None or "auth_date" not in data or "id" not in data:
        raise TelegramAuthError("Incomplete Telegram widget data")
    if any(isinstance(value, (dict, list, tuple, bool)) for value in data.values()):
        raise TelegramAuthError("Invalid Telegram widget data")

    data_check_string = "\n".join(
        f"{key}={value}" for key, value in sorted(data.items())
    )
    token = bot_token if bot_token is not None else settings.telegram_bot_token
    if not token:
        raise TelegramAuthError("Telegram bot token is not configured")
    secret_key = hashlib.sha256(token.encode()).digest()
    expected_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256,
    ).hexdigest()
    _validate_hash(received_hash, expected_hash)
    _validate_auth_date(data["auth_date"], now)
    return _identity_from_user(data)
