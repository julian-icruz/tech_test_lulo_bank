from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException, Depends

from app.transform.container import TransformContainer
from app.transform.application.services import DataCleaninOrchestrationService

from app.file_io.application.dtos import ReaderConfigDTO, WriterConfigDTO, PathIODTO

router = APIRouter()


@router.post("/cleaning", summary="Generate a data cleaning report")
@inject
def data_cleaning(
    reader_config: ReaderConfigDTO,
    writer_config: WriterConfigDTO,
    path_io: PathIODTO,
    data_cleaning_service: DataCleaninOrchestrationService = Depends(
        Provide[TransformContainer.data_cleaning_orchestration_service]
    ),
):
    """
    Generates a profiling report based on the provided configurations.
    """
    try:
        data_cleaning_service(
            writer_config=writer_config, reader_config=reader_config, path_io=path_io
        )
        return {
            "message": "Data cleaning report generated successfully.",
            "reader": reader_config,
            "writer": writer_config,
            "path_io": path_io,
        }
    except Exception as e:
        print(f"Failed to generate cleaning: {str(e)}")
        raise HTTPException(status_code=500)
