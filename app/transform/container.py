from dependency_injector.providers import Dependency, Singleton, Dict
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.transform.infrastructure.adapters import (
    ReportGeneratorAdapter,
    PandasProfiling,
    PolarsProfiling,
    DaskProfiling,
)
from app.transform.application.services import (
    ProfilingService,
    ProfilingReportService,
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

    profiling_adapters = Dict(
        pandas=PandasProfiling,
        polars=PolarsProfiling,
        dask=DaskProfiling,
    )

    profiling_service = Singleton(
        ProfilingService,
        profiling_adapters=profiling_adapters,
    )

    reader_writer_selector = Dependency(instance_of=ReaderWriterSelectorService)

    profiling_report_service = Singleton(
        ProfilingReportService,
        profiling_service=profiling_service,
        report_generator=report_generator_adapter,
        reader_writer_selector=reader_writer_selector,
    )
