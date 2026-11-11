import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Uuid

from app.db.base_class import Base
from app.models.user import generate_uuid7


class FeatureKey(str, enum.Enum):
    CODE_MARKETPLACE = "code_marketplace"
    PRO_ANALYTICS = "pro_analytics"
    AUTO_REPRICER = "auto_repricer"


class TokenSymbol(str, enum.Enum):
    USDC = "USDC"
    TON = "TON"
    WBTC = "WBTC"
    SOL = "SOL"


class FeatureWaitlist(Base):
    __tablename__ = "feature_waitlist"
    __table_args__ = (
        UniqueConstraint(
            "wallet_address",
            "feature_key",
            name="uq_feature_waitlist_wallet_feature",
        ),
        CheckConstraint(
            "user_id IS NOT NULL OR wallet_address IS NOT NULL",
            name="ck_feature_waitlist_identity",
        ),
        CheckConstraint(
            "wallet_address IS NULL OR wallet_address = lower(wallet_address)",
            name="ck_feature_waitlist_wallet_lowercase",
        ),
        CheckConstraint(
            "feature_key IN ('code_marketplace', 'pro_analytics', 'auto_repricer')",
            name="ck_feature_waitlist_feature_key",
        ),
        Index("ix_feature_waitlist_feature_key", "feature_key"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=generate_uuid7,
    )
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    wallet_address: Mapped[str | None] = mapped_column(String(42), nullable=True)
    feature_key: Mapped[FeatureKey] = mapped_column(String(32), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        nullable=False,
    )


class TokenVote(Base):
    __tablename__ = "token_votes"
    __table_args__ = (
        UniqueConstraint("user_id", name="uq_token_votes_user_id"),
        CheckConstraint(
            "token_symbol IN ('USDC', 'TON', 'WBTC', 'SOL')",
            name="ck_token_votes_token_symbol",
        ),
        Index("ix_token_votes_token_symbol", "token_symbol"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=generate_uuid7,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    token_symbol: Mapped[TokenSymbol] = mapped_column(String(8), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
