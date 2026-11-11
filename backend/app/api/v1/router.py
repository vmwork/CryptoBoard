from fastapi import APIRouter, Depends

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.listings import router as listings_router
from app.api.v1.endpoints.waitlist import router as waitlist_router
from app.core.security import require_internal_bff_secret

router = APIRouter(dependencies=[Depends(require_internal_bff_secret)])
router.include_router(auth_router)
router.include_router(listings_router)
router.include_router(waitlist_router)
