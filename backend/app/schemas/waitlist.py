import re
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.models.waitlist import FeatureKey, TokenSymbol


class WaitlistJoinRequest(BaseModel):
    wallet_address: str | None = Field(default=None, min_length=42, max_length=42)
    feature_key: FeatureKey

    @field_validator("wallet_address")
    @classmethod
    def normalize_wallet_address(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if not re.fullmatch(r"0x[0-9a-fA-F]{40}", value):
            raise ValueError("invalid EVM wallet address")
        return value.lower()


class WaitlistEntryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    feature_key: FeatureKey
    created_at: datetime


class TokenVoteRequest(BaseModel):
    token_symbol: TokenSymbol

    @field_validator("token_symbol", mode="before")
    @classmethod
    def normalize_token_symbol(cls, value: object) -> object:
        return value.upper() if isinstance(value, str) else value


class TokenVoteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    token_symbol: TokenSymbol
    created_at: datetime


class FeatureWaitlistCounts(BaseModel):
    code_marketplace: int = 0
    pro_analytics: int = 0
    auto_repricer: int = 0


class TokenVoteCounts(BaseModel):
    USDC: int = 0
    TON: int = 0
    WBTC: int = 0
    SOL: int = 0


class WaitlistStatsResponse(BaseModel):
    waitlist: FeatureWaitlistCounts
    token_votes: TokenVoteCounts
