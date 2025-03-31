from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException, Depends

# from app.container import AppContainer
from app.load.container import LoadContainer
from app.load.application.services import LoadOrchestrationService

from app.file_io.application.dtos import ReaderConfigDTO, PathIODTO

router = APIRouter()


@router.post("/to_db", summary="Load data to database")
@inject
def load_db(
    database: str,
    reader_config: ReaderConfigDTO,
    path_io: PathIODTO,
    load_service: LoadOrchestrationService = Depends(
        Provide[LoadContainer.load_orchestration_service]
    ),
):
    """
    Generates a profiling report based on the provided configurations.
    """
    try:
        load_service(
            path_io=path_io,
            reader_config=reader_config,
            database=database,
        )
        return {
            "message": "Data loaded to database successfully.",
            "reader": reader_config,
            "path_io": path_io,
            "database": database,
        }
    except Exception as e:
        print(f"Failed to load data to database: {str(e)}")
        raise HTTPException(status_code=500)
