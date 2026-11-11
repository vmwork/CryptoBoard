import enum
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Numeric,
    String,
    Text,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Uuid

from app.db.base_class import Base
from app.models.user import generate_uuid7


class ListingCategory(str, enum.Enum):
    GPU = "gpu"
    CPU = "cpu"
    RAM = "ram"
    MINING = "mining"
    SMARTPHONE = "smartphone"
    OTHER = "other"


class ListingCondition(str, enum.Enum):
    NEW = "new"
    USED = "used"
    REFURBISHED = "refurbished"


class ListingStatus(str, enum.Enum):
    ACTIVE = "active"
    RESERVED = "reserved"
    SOLD = "sold"
    ARCHIVED = "archived"


class Listing(Base):
    __tablename__ = "listings"
    __table_args__ = (
        CheckConstraint("price_usdt > 0", name="ck_listings_price_positive"),
        Index("ix_listings_seller_status", "seller_id", "status"),
        Index("ix_listings_public_filters", "status", "category", "condition"),
        Index("ix_listings_created_at", "created_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=generate_uuid7,
    )
    seller_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[ListingCategory] = mapped_column(
        Enum(
            ListingCategory,
            name="listing_category",
            values_callable=lambda members: [member.value for member in members],
            validate_strings=True,
        ),
        nullable=False,
    )
    condition: Mapped[ListingCondition] = mapped_column(
        Enum(
            ListingCondition,
            name="listing_condition",
            values_callable=lambda members: [member.value for member in members],
            validate_strings=True,
        ),
        nullable=False,
    )
    price_usdt: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    serial_number: Mapped[str | None] = mapped_column(String(128), nullable=True)
    stress_test_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    images: Mapped[list[str]] = mapped_column(
        JSONB,
        default=list,
        server_default=text("'[]'::jsonb"),
        nullable=False,
    )
    status: Mapped[ListingStatus] = mapped_column(
        Enum(
            ListingStatus,
            name="listing_status",
            values_callable=lambda members: [member.value for member in members],
            validate_strings=True,
        ),
        default=ListingStatus.ACTIVE,
        server_default=ListingStatus.ACTIVE.value,
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
