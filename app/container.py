from dependency_injector import containers

from app.file_io import FileIOContainer
from app.db_connections import DBConnectionsContainer
from app.extract import ExtractContainer
from app.transform import TransformContainer
from app.load import LoadContainer


class AppContainer(containers.DeclarativeContainer):
    file_io = FileIOContainer()
    db_connections = DBConnectionsContainer()
    extract = ExtractContainer(
        file_io=file_io,
    )
    transform = TransformContainer(
        reader_writer_selector=file_io.reader_writer_selector_service,
    )
    load = LoadContainer(
        reader_writer_selector=file_io.reader_writer_selector_service,
        database_connection_service=db_connections.database_connection_service,
    )
