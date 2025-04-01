from dependency_injector.providers import Dependency, Singleton
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.load.infrastructure.adapters import PostgresLoaderAdapter
from app.load.application.services import LoadOrchestrationService

from app.file_io.application.services import ReaderWriterSelectorService

from app.db_connections.application.services import DatabaseConnectionService


class LoadContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=[
            "app.load.routes",
        ]
    )

    reader_writer_selector = Dependency(instance_of=ReaderWriterSelectorService)
    database_connection_service = Dependency(instance_of=DatabaseConnectionService)

    postgres_loader_adapter = Singleton(
        PostgresLoaderAdapter,
        db_service=database_connection_service,
    )

    load_orchestration_service = Singleton(
        LoadOrchestrationService,
        reader_writer_selector=reader_writer_selector,
        data_loader_adapter=postgres_loader_adapter,
    )
