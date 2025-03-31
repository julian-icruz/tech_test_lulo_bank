from dependency_injector.providers import Dependency, Singleton, Dict, Callable
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.transform.infrastructure.adapters import ReportGeneratorAdapter
from app.transform.application.services import (
    ProfilingService,
    ProfilingReportService,
)


class TransformContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=[
            "app.transform.routes",
        ]
    )

    file_io = Dependency()

    report_generator_adapter = Singleton(ReportGeneratorAdapter)

    profiling_adapters = Dict()

    profiling_service = Singleton(
        ProfilingService,
        profiling_adapters=profiling_adapters,
    )

    profiling_report_service = Singleton(
        ProfilingReportService,
        profiling_service=profiling_service,
        report_generator=report_generator_adapter,
        reader_writer_selector=Callable(
            lambda file_io: file_io.reader_writer_selector_service, file_io
        ),
    )
