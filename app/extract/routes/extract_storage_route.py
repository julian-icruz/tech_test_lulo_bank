from fastapi import APIRouter, HTTPException, Depends
from dependency_injector.wiring import inject, Provide

from app.extract.container import ExtractContainer
from app.extract.application.services import ExtractStorageService

from app.file_io.application.dtos import WriterConfigDTO

router = APIRouter()


@router.post("/storage", summary="Extract and store TV schedule data")
@inject
async def store_schedule(
    date: str,
    writer_config: WriterConfigDTO,
    storage_service: ExtractStorageService = Depends(
        Provide[ExtractContainer.extract_storage_service]
    ),
):
    """
    Extracts TV schedule data for the specified date and stores each entry as a file.

    Parameters:
        - date (str): The schedule date in 'YYYY-MM-DD' format (as a query parameter).
        - writer_config (WriterConfigDTO): JSON body with writer configuration details.

    Returns:
        A message indicating that the schedule was stored successfully.
    """
    try:
        count = await storage_service.extract_and_store(date, writer_config)
        return {
            "message": f"Schedule {date} stored successfully.",
            "details": writer_config,
            "files_stored": count,
        }
    except Exception:
        raise HTTPException(status_code=500)
