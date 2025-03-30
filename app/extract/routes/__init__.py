from fastapi import APIRouter

from app.extract.routes import extract_route

router = APIRouter(prefix="/extract", tags=["Extract"])

router.include_router(extract_route.router)
