import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, String, func
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
            "wallet_address = lower(wallet_address)",
            name="ck_users_wallet_address_lowercase",
        ),
        Index("ix_users_wallet_address", "wallet_address", unique=True),
        Index("ix_users_referrer_id", "referrer_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=generate_uuid7,
    )
    wallet_address: Mapped[str] = mapped_column(String(42), nullable=False)
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
