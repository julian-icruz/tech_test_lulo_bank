from fastapi import APIRouter

from app.transform.routes import (
    profiling_route,
)

router = APIRouter(prefix="/transform", tags=["Transform"])

router.include_router(profiling_route.router)
