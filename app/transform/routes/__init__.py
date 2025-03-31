from fastapi import APIRouter

from app.transform.routes import (
    profiling_route,
    data_cleaning_route,
)

router = APIRouter(prefix="/transform", tags=["Transform"])

router.include_router(profiling_route.router)
router.include_router(data_cleaning_route.router)
