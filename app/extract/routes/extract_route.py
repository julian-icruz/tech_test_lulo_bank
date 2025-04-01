from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException, Depends

from app.extract.container import ExtractContainer
from app.extract.domain.services import ExtractService


router = APIRouter()


@router.get("/schedule", response_model=list[dict])
@inject
async def get_tv_schedule(
    date: str,
    extract_service: ExtractService = Depends(
        Provide[ExtractContainer.extract_service]
    ),
) -> list[dict]:
    """
    Endpoint to fetch the TV schedule for a given date.
    """
    try:
        schedule = await extract_service.get_schedule(date)
        return schedule
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch schedule: {str(e)}"
        )
