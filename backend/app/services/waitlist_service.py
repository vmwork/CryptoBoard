from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.waitlist import FeatureKey, FeatureWaitlist, TokenSymbol, TokenVote
from app.schemas.waitlist import (
    FeatureWaitlistCounts,
    TokenVoteCounts,
    WaitlistEntryResponse,
    WaitlistJoinRequest,
    WaitlistStatsResponse,
)


def join_waitlist(
    db: Session,
    payload: WaitlistJoinRequest,
    current_user: User | None = None,
) -> FeatureWaitlist:
    wallet_address = payload.wallet_address
    if current_user is not None:
        if wallet_address is not None and wallet_address != current_user.wallet_address:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "WALLET_MISMATCH", "message": "Wallet does not match the session"},
            )
        wallet_address = current_user.wallet_address
    if wallet_address is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"code": "WALLET_REQUIRED", "message": "wallet_address or a linked wallet session is required"},
        )

    existing = db.scalar(
        select(FeatureWaitlist).where(
            FeatureWaitlist.wallet_address == wallet_address,
            FeatureWaitlist.feature_key == payload.feature_key.value,
        )
    )
    if existing is not None:
        if existing.user_id is None and current_user is not None:
            existing.user_id = current_user.id
            db.add(existing)
            db.commit()
            db.refresh(existing)
        return existing

    entry = FeatureWaitlist(
        user_id=current_user.id if current_user is not None else None,
        wallet_address=wallet_address,
        feature_key=payload.feature_key,
    )
    db.add(entry)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        existing = db.scalar(
            select(FeatureWaitlist).where(
                FeatureWaitlist.wallet_address == wallet_address,
                FeatureWaitlist.feature_key == payload.feature_key.value,
            )
        )
        if existing is None:
            raise
        return existing
    db.refresh(entry)
    return entry


def cast_token_vote(db: Session, user: User, token_symbol: TokenSymbol) -> TokenVote:
    existing = db.scalar(select(TokenVote).where(TokenVote.user_id == user.id))
    if existing is not None:
        if existing.token_symbol == token_symbol.value:
            return existing
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"code": "VOTE_ALREADY_CAST", "message": "Only one token vote is allowed"},
        )

    vote = TokenVote(user_id=user.id, token_symbol=token_symbol)
    db.add(vote)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        existing = db.scalar(select(TokenVote).where(TokenVote.user_id == user.id))
        if existing is None:
            raise
        if existing.token_symbol == token_symbol.value:
            return existing
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"code": "VOTE_ALREADY_CAST", "message": "Only one token vote is allowed"},
        )
    db.refresh(vote)
    return vote


def get_waitlist_stats(db: Session) -> WaitlistStatsResponse:
    waitlist_counts = {
        key.value: 0
        for key in FeatureKey
    }
    for feature_key, count in db.execute(
        select(FeatureWaitlist.feature_key, func.count(FeatureWaitlist.id))
        .group_by(FeatureWaitlist.feature_key)
    ):
        key = feature_key.value if isinstance(feature_key, FeatureKey) else feature_key
        if key in waitlist_counts:
            waitlist_counts[key] = int(count)

    token_counts = {symbol.value: 0 for symbol in TokenSymbol}
    for token_symbol, count in db.execute(
        select(TokenVote.token_symbol, func.count(TokenVote.id))
        .group_by(TokenVote.token_symbol)
    ):
        symbol = token_symbol.value if isinstance(token_symbol, TokenSymbol) else token_symbol
        if symbol in token_counts:
            token_counts[symbol] = int(count)

    return WaitlistStatsResponse(
        waitlist=FeatureWaitlistCounts(**waitlist_counts),
        token_votes=TokenVoteCounts(**token_counts),
    )
