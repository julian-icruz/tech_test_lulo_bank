from dependency_injector.providers import Singleton, Dependency
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from app.extract.domain.services import ExtractService
from app.extract.infrastructure.adapters.http import TVMazeAPIAdapter


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
