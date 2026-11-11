from fastapi import APIRouter, status

from app.api.dependencies import CurrentUser, DbSession, OptionalCurrentUser
from app.schemas.waitlist import (
    TokenVoteRequest,
    TokenVoteResponse,
    WaitlistEntryResponse,
    WaitlistJoinRequest,
    WaitlistStatsResponse,
)
from app.services import waitlist_service

router = APIRouter(prefix="/waitlist", tags=["waitlist"])


@router.post("", response_model=WaitlistEntryResponse, status_code=status.HTTP_201_CREATED)
def join_waitlist(
    payload: WaitlistJoinRequest,
    db: DbSession,
    current_user: OptionalCurrentUser,
) -> WaitlistEntryResponse:
    return WaitlistEntryResponse.model_validate(
        waitlist_service.join_waitlist(db, payload, current_user)
    )


@router.post("/vote", response_model=TokenVoteResponse, status_code=status.HTTP_201_CREATED)
def vote_for_token(
    payload: TokenVoteRequest,
    db: DbSession,
    current_user: CurrentUser,
) -> TokenVoteResponse:
    return TokenVoteResponse.model_validate(
        waitlist_service.cast_token_vote(db, current_user, payload.token_symbol)
    )


@router.get("/stats", response_model=WaitlistStatsResponse)
def read_waitlist_stats(db: DbSession) -> WaitlistStatsResponse:
    return waitlist_service.get_waitlist_stats(db)
