from dependency_injector.providers import Dependency
from dependency_injector.containers import DeclarativeContainer


class TransformContainer(DeclarativeContainer):

    file_io = Dependency()
