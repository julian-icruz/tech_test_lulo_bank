from fastapi import APIRouter

from app.load.routes import (
    load_to_db_route,
)

router = APIRouter(prefix="/load", tags=["Load"])

router.include_router(load_to_db_route.router)
