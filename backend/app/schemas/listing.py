import uuid
from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

from app.models.listing import ListingCategory, ListingCondition, ListingStatus

ImagePath = Annotated[str, StringConstraints(min_length=1, max_length=1024)]


class ListingCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=10000)
    category: ListingCategory
    condition: ListingCondition
    price_usdt: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    serial_number: str | None = Field(default=None, max_length=128)
    stress_test_url: str | None = Field(default=None, max_length=2048)
    images: list[ImagePath] = Field(default_factory=list, max_length=20)
    status: ListingStatus = ListingStatus.ACTIVE


class ListingUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, min_length=1, max_length=10000)
    category: ListingCategory | None = None
    condition: ListingCondition | None = None
    price_usdt: Annotated[
        Decimal,
        Field(gt=0, max_digits=12, decimal_places=2),
    ] | None = None
    serial_number: str | None = Field(default=None, max_length=128)
    stress_test_url: str | None = Field(default=None, max_length=2048)
    images: list[ImagePath] | None = Field(default=None, max_length=20)
    status: ListingStatus | None = None

    @model_validator(mode="after")
    def validate_patch(self):
        if not self.model_fields_set:
            raise ValueError("at least one field must be provided")
        for field_name in (
            "title",
            "description",
            "category",
            "condition",
            "price_usdt",
            "images",
            "status",
        ):
            if field_name in self.model_fields_set and getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")
        return self


class ListingPublicRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str
    category: ListingCategory
    condition: ListingCondition
    price_usdt: Decimal
    stress_test_url: str | None
    images: list[str]
    status: ListingStatus
    created_at: datetime
    updated_at: datetime


class ListingRead(ListingPublicRead):
    seller_id: uuid.UUID
    serial_number: str | None


class ListingListResponse(BaseModel):
    items: list[ListingPublicRead]
    total: int
    page: int
    page_size: int
    pages: int
