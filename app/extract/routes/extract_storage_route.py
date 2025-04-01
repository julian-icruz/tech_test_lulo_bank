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
    """
    try:
        count = await storage_service.extract_and_store(date, writer_config)
        return {
            "message": f"Schedule {date} stored successfully.",
            "details": writer_config,
            "files_stored": count,
        }
    except Exception as e:
        print(f"Error extracting and storing schedule: {e}")
        raise HTTPException(status_code=500)
