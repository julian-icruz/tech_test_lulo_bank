from dependency_injector import containers

from file_io import FileIOContainer


class AppContainer(containers.DeclarativeContainer):
    file_io = FileIOContainer()
