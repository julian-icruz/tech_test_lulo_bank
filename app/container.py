from dependency_injector import containers

from app.file_io import FileIOContainer


class AppContainer(containers.DeclarativeContainer):
    file_io = FileIOContainer()
