from dependency_injector import containers

from app.file_io import FileIOContainer
from app.db_connections import DBConnectionsContainer
from app.extract import ExtractContainer
from app.transform import TransformContainer


class AppContainer(containers.DeclarativeContainer):
    file_io = FileIOContainer()
    db_connections = DBConnectionsContainer()
    extract = ExtractContainer(
        file_io=file_io,
    )
    transform = TransformContainer(
        file_io=file_io,
    )
