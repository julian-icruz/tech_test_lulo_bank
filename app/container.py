from dependency_injector import containers

from app.file_io import FileIOContainer
from app.db_connections import DBConnectionsContainer
from app.extract import ExtractContainer


class AppContainer(containers.DeclarativeContainer):
    file_io = FileIOContainer()
    db_connections = DBConnectionsContainer()
    extract = ExtractContainer()
