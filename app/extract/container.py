from dependency_injector.providers import Singleton, Dependency, Callable
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.extract.infrastructure.adapters.http import TVMazeAPIAdapter
from app.extract.domain.services import ExtractService
from app.extract.application.services import ExtractStorageService


class ExtractContainer(DeclarativeContainer):
    """
    Dependency Injection Container for the Extract context.

    This container manages the dependencies required for the Extract context, such as
    the TvMazeAPI and ExtractService.
    """

    wiring_config = WiringConfiguration(
        packages=[
            "app.extract.routes",
        ]
    )

    file_io = Dependency()

    tvmaze_api_adapter = Singleton(TVMazeAPIAdapter)

    extract_service = Singleton(
        ExtractService,
        extractor_adapter=tvmaze_api_adapter,
    )

    extract_storage_service = Singleton(
        ExtractStorageService,
        extract_service=extract_service,
        writers=Callable(lambda file_io: file_io.writers, file_io),
    )
