import uuid
from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Query, Response, status

from app.api.dependencies import Cache, CurrentUser, DbSession
from app.models.listing import ListingCategory, ListingCondition
from app.schemas.listing import (
    ListingCreate,
    ListingListResponse,
    ListingPublicRead,
    ListingRead,
    ListingUpdate,
)
from app.services import listing_service

router = APIRouter(prefix="/listings", tags=["listings"])


@router.get("", response_model=ListingListResponse)
def read_listings(
    db: DbSession,
    category: Annotated[ListingCategory | None, Query()] = None,
    condition: Annotated[ListingCondition | None, Query()] = None,
    min_price: Annotated[Decimal | None, Query(ge=0)] = None,
    max_price: Annotated[Decimal | None, Query(ge=0)] = None,
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 20,
) -> ListingListResponse:
    return listing_service.list_public_listings(
        db,
        category=category,
        condition=condition,
        min_price=min_price,
        max_price=max_price,
        page=page,
        page_size=page_size,
    )


@router.get("/{listing_id}", response_model=ListingPublicRead)
def read_listing(listing_id: uuid.UUID, db: DbSession) -> ListingPublicRead:
    return ListingPublicRead.model_validate(
        listing_service.get_public_listing(db, listing_id)
    )


@router.post("", response_model=ListingRead, status_code=status.HTTP_201_CREATED)
def create_listing(
    payload: ListingCreate,
    db: DbSession,
    cache: Cache,
    current_user: CurrentUser,
) -> ListingRead:
    return ListingRead.model_validate(
        listing_service.create_listing(db, cache, current_user, payload)
    )


@router.patch("/{listing_id}", response_model=ListingRead)
def update_listing(
    listing_id: uuid.UUID,
    payload: ListingUpdate,
    db: DbSession,
    cache: Cache,
    current_user: CurrentUser,
) -> ListingRead:
    return ListingRead.model_validate(
        listing_service.update_listing(db, cache, listing_id, current_user, payload)
    )


@router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_listing(
    listing_id: uuid.UUID,
    db: DbSession,
    current_user: CurrentUser,
) -> Response:
    listing_service.archive_listing(db, listing_id, current_user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
