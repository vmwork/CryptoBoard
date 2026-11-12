import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Uuid
from uuid_utils import uuid7

from app.db.base_class import Base


def generate_uuid7() -> uuid.UUID:
    return uuid.UUID(bytes=uuid7().bytes)


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "wallet_address IS NULL OR wallet_address = lower(wallet_address)",
            name="ck_users_wallet_address_lowercase",
        ),
        CheckConstraint(
            "wallet_address IS NOT NULL OR telegram_id IS NOT NULL",
            name="ck_users_identity",
        ),
        Index("ix_users_wallet_address", "wallet_address", unique=True),
        Index("ix_users_referrer_id", "referrer_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=generate_uuid7,
    )
    wallet_address: Mapped[str | None] = mapped_column(String(42), nullable=True)
    telegram_id: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True,
        index=True,
        unique=True,
    )
    telegram_username: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
    )
    first_name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    referrer_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    has_passport: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )
