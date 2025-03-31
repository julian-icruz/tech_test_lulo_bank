from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException, Depends

from app.transform.container import TransformContainer
from app.transform.application.services import ProfilingReportService

from app.file_io.application.dtos import ReaderConfigDTO, WriterConfigDTO, PathIODTO

router = APIRouter()


@router.get("/profiling", summary="Generate a profiling report")
@inject
def get_tv_schedule(
    reader_config: ReaderConfigDTO,
    writer_config: WriterConfigDTO,
    path_io: PathIODTO,
    profiling_report_service: ProfilingReportService = Depends(
        Provide[TransformContainer.profiling_report_service]
    ),
):
    """
    Generates a profiling report based on the provided configurations.
    """
    try:
        profiling_report_service(
            writer_config=writer_config, reader_config=reader_config, path_io=path_io
        )
        return {
            "message": "Profiling report generated successfully.",
            "reader": reader_config,
            "writer": writer_config,
            "path_io": path_io,
        }
    except Exception as e:
        print(f"Failed to generate profiling report: {str(e)}")
        raise HTTPException(status_code=500)
