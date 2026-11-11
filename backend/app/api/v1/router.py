from fastapi import APIRouter, Depends

from app.api.v1.endpoints.auth import router as auth_router
from app.core.security import require_internal_bff_secret

router = APIRouter(dependencies=[Depends(require_internal_bff_secret)])
router.include_router(auth_router)
