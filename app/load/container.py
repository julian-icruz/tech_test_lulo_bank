from dependency_injector.providers import Dependency
from dependency_injector.containers import DeclarativeContainer

from app.file_io.application.services import ReaderWriterSelectorService
from app.db_connections.application.services import DatabaseConnectionService


class LoadContainer(DeclarativeContainer):

    reader_writer_selector = Dependency(instance_of=ReaderWriterSelectorService)
    database_connection_service = Dependency(instance_of=DatabaseConnectionService)
