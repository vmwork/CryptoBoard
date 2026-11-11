from decimal import Decimal
from typing import Any

import httpx
from fastapi import HTTPException, status
from redis import Redis
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.listing import Listing, ListingCategory, ListingCondition, ListingStatus
from app.models.user import User
from app.schemas.listing import (
    ListingCreate,
    ListingListResponse,
    ListingPublicRead,
    ListingUpdate,
)

FREE_ACTIVE_LISTING_LIMIT = 3
PASSPORT_ACTIVE_LISTING_LIMIT = 10
TRANSACTION_COUNT_CACHE_TTL = 24 * 60 * 60


def _transaction_count_cache_key(wallet_address: str) -> str:
    return (
        f"listings:outgoing_transactions:{settings.evm_chain_id}:"
        f"{wallet_address.lower()}"
    )


def _rpc_transaction_count(wallet_address: str) -> int:
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionCount",
        "params": [wallet_address.lower(), "latest"],
        "id": 1,
    }
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(settings.evm_rpc_url, json=payload)
            response.raise_for_status()
            result = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "RPC_UNAVAILABLE", "message": "Wallet activity is unavailable"},
        ) from exc

    if not isinstance(result, dict) or result.get("error") is not None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "RPC_UNAVAILABLE", "message": "Wallet activity is unavailable"},
        )
    value = result.get("result")
    if not isinstance(value, str):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "RPC_UNAVAILABLE", "message": "Wallet activity is unavailable"},
        )
    try:
        count = int(value, 16)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "RPC_UNAVAILABLE", "message": "Wallet activity is unavailable"},
        ) from exc
    if count < 0:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "RPC_UNAVAILABLE", "message": "Wallet activity is unavailable"},
        )
    return count


def get_outgoing_transaction_count(wallet_address: str, cache: Redis) -> int:
    key = _transaction_count_cache_key(wallet_address)
    cached = cache.get(key)
    if cached is not None:
        if isinstance(cached, bytes):
            cached = cached.decode()
        try:
            count = int(cached)
        except (TypeError, ValueError):
            cache.delete(key)
        else:
            if count >= 0:
                return count
            cache.delete(key)

    count = _rpc_transaction_count(wallet_address)
    cache.set(key, str(count), ex=TRANSACTION_COUNT_CACHE_TTL)
    return count


def _active_listing_count(db: Session, seller_id: Any, exclude_id: Any = None) -> int:
    query = select(func.count(Listing.id)).where(
        Listing.seller_id == seller_id,
        Listing.status == ListingStatus.ACTIVE,
    )
    if exclude_id is not None:
        query = query.where(Listing.id != exclude_id)
    return int(db.scalar(query) or 0)


def enforce_active_listing_limit(
    db: Session,
    cache: Redis,
    seller: User,
    exclude_id: Any = None,
) -> None:
    locked_seller = db.scalar(
        select(User).where(User.id == seller.id).with_for_update()
    )
    if locked_seller is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session is invalid",
        )
    limit = (
        PASSPORT_ACTIVE_LISTING_LIMIT
        if locked_seller.has_passport
        else FREE_ACTIVE_LISTING_LIMIT
    )
    if _active_listing_count(db, locked_seller.id, exclude_id) >= limit:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": "LISTING_LIMIT_REACHED",
                "message": f"Active listing limit is {limit}",
                "limit": limit,
            },
        )
    if not locked_seller.has_passport and get_outgoing_transaction_count(
        locked_seller.wallet_address,
        cache,
    ) == 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": "PASSPORT_REQUIRED",
                "message": "A seller passport is required for wallets without transactions",
            },
        )


def list_public_listings(
    db: Session,
    category: ListingCategory | None = None,
    condition: ListingCondition | None = None,
    min_price: Decimal | None = None,
    max_price: Decimal | None = None,
    page: int = 1,
    page_size: int = 20,
) -> ListingListResponse:
    if min_price is not None and max_price is not None and min_price > max_price:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="min_price must not exceed max_price",
        )
    filters = [Listing.status == ListingStatus.ACTIVE]
    if category is not None:
        filters.append(Listing.category == category)
    if condition is not None:
        filters.append(Listing.condition == condition)
    if min_price is not None:
        filters.append(Listing.price_usdt >= min_price)
    if max_price is not None:
        filters.append(Listing.price_usdt <= max_price)

    total = int(db.scalar(select(func.count(Listing.id)).where(*filters)) or 0)
    listings = db.scalars(
        select(Listing)
        .where(*filters)
        .order_by(Listing.created_at.desc(), Listing.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    ).all()
    return ListingListResponse(
        items=[ListingPublicRead.model_validate(listing) for listing in listings],
        total=total,
        page=page,
        page_size=page_size,
        pages=(total + page_size - 1) // page_size,
    )


def get_public_listing(db: Session, listing_id: Any) -> Listing:
    listing = db.get(Listing, listing_id)
    if listing is None or listing.status == ListingStatus.ARCHIVED:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Listing not found",
        )
    return listing


def create_listing(
    db: Session,
    cache: Redis,
    seller: User,
    payload: ListingCreate,
) -> Listing:
    if payload.status == ListingStatus.ACTIVE:
        enforce_active_listing_limit(db, cache, seller)
    listing = Listing(
        seller_id=seller.id,
        **payload.model_dump(),
    )
    db.add(listing)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(listing)
    return listing


def get_owned_listing(db: Session, listing_id: Any, seller: User) -> Listing:
    listing = db.get(Listing, listing_id)
    if listing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Listing not found",
        )
    if listing.seller_id != seller.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "NOT_LISTING_OWNER", "message": "You do not own this listing"},
        )
    return listing


def update_listing(
    db: Session,
    cache: Redis,
    listing_id: Any,
    seller: User,
    payload: ListingUpdate,
) -> Listing:
    listing = get_owned_listing(db, listing_id, seller)
    changes = payload.model_dump(exclude_unset=True)
    new_status = changes.get("status")
    if new_status == ListingStatus.ACTIVE and listing.status != ListingStatus.ACTIVE:
        enforce_active_listing_limit(db, cache, seller, exclude_id=listing.id)
    for field_name, value in changes.items():
        setattr(listing, field_name, value)
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


def archive_listing(db: Session, listing_id: Any, seller: User) -> None:
    listing = get_owned_listing(db, listing_id, seller)
    listing.status = ListingStatus.ARCHIVED
    db.add(listing)
    db.commit()
