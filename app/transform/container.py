from dependency_injector.providers import Dependency, Singleton
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

    profiling_service = Singleton(
        ProfilingService,
        report_generator_adapter=report_generator_adapter,
    )
