from dependency_injector.providers import Dependency, Singleton, Dict
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.transform.infrastructure.adapters import (
    ReportGeneratorAdapter,
    PandasProfiling,
    PandasTransformation,
    PolarsProfiling,
    PolarsTransformation,
    DaskProfiling,
    DaskTransformation,
)
from app.transform.domain.services import (
    ProfilingService,
    DataCleaningService,
)
from app.transform.application.services import (
    ProfilingReportService,
    DataCleaninOrchestrationService,
)

from app.file_io.application.services import ReaderWriterSelectorService


class TransformContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=[
            "app.transform.routes",
        ]
    )

    report_generator_adapter = Singleton(ReportGeneratorAdapter)

    pandas_profiling_adapter = Singleton(PandasProfiling)
    polars_profiling_adapter = Singleton(PolarsProfiling)
    dask_profiling_adapter = Singleton(DaskProfiling)

    pandas_transformation_adapter = Singleton(PandasTransformation)
    polars_transformation_adapter = Singleton(PolarsTransformation)
    dask_transformation_adapter = Singleton(DaskTransformation)

    profiling_adapters = Dict(
        pandas=pandas_profiling_adapter,
        polars=polars_profiling_adapter,
        dask=dask_profiling_adapter,
    )

    transformation_adapters = Dict(
        pandas=pandas_transformation_adapter,
        polars=polars_transformation_adapter,
        dask=dask_transformation_adapter,
    )

    profiling_service = Singleton(
        ProfilingService,
        profiling_adapters=profiling_adapters,
        transformation_adapters=transformation_adapters,
    )

    data_cleaning_service = Singleton(
        DataCleaningService,
        profiling_adapters=profiling_adapters,
        transformation_adapters=transformation_adapters,
    )

    reader_writer_selector = Dependency(instance_of=ReaderWriterSelectorService)

    profiling_report_service = Singleton(
        ProfilingReportService,
        profiling_service=profiling_service,
        report_generator=report_generator_adapter,
        reader_writer_selector=reader_writer_selector,
    )

    data_cleaning_orchestration_service = Singleton(
        DataCleaninOrchestrationService,
        data_cleaning_service=data_cleaning_service,
        reader_writer_selector=reader_writer_selector,
    )
