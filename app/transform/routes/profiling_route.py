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
    Generates a data profiling report using the provided configuration DTOs.

    This endpoint performs the following steps:
        1. Reads the input data using the file reader defined by reader_config.
        2. Processes the data with the profiling service to obtain descriptive statistics,
            missing values, duplicates, correlations, and column type profiles.
        3. Generates an HTML report using the report generator adapter.
        4. Writes the report to the output path specified in path_io, ensuring the output directory exists.

    Args:
        reader_config (ReaderConfigDTO): Configuration for selecting the file reader.
        writer_config (WriterConfigDTO): Configuration for selecting the file writer.
        path_io (PathIODTO): DTO containing the input path, output path, and an optional bucket.
        profiling_report_service (ProfilingReportService): Service used to generate and write the profiling report.

    Returns:
        dict: A JSON object containing a success message along with the reader, writer, and path configuration details.

    Raises:
        HTTPException: If any error occurs during the profiling report generation process.
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
