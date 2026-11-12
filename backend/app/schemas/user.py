import re
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NonceRequest(BaseModel):
    wallet_address: str = Field(min_length=42, max_length=42)

    @field_validator("wallet_address")
    @classmethod
    def normalize_wallet_address(cls, value: str) -> str:
        if not re.fullmatch(r"0x[0-9a-fA-F]{40}", value):
            raise ValueError("invalid EVM wallet address")
        return value.lower()


class NonceResponse(BaseModel):
    nonce: str
    expires_in: int


class VerifyRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4096)
    signature: str = Field(pattern=r"^0x[0-9a-fA-F]{130}$")


class TelegramWebAppRequest(BaseModel):
    init_data: str = Field(min_length=1, max_length=8192, alias="initData")

    model_config = ConfigDict(populate_by_name=True)


class TelegramWidgetRequest(BaseModel):
    id: int = Field(gt=0)
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str | None = Field(default=None, max_length=64)
    username: str | None = Field(default=None, max_length=32)
    photo_url: str | None = Field(default=None, max_length=2048)
    auth_date: int = Field(gt=0)
    hash: str = Field(pattern=r"^[0-9a-fA-F]{64}$")


class LinkWalletRequest(VerifyRequest):
    pass


class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    wallet_address: str | None
    telegram_id: int | None
    telegram_username: str | None
    first_name: str | None
    avatar_url: str | None
    referrer_id: uuid.UUID | None
    has_passport: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime


class VerifyResponse(BaseModel):
    user: UserProfile
    expires_in: int


class InternalVerifyResponse(VerifyResponse):
    session_id: str


class LogoutResponse(BaseModel):
    success: bool
