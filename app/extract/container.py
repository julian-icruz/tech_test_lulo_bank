from dependency_injector import containers, providers

from app.extract.domain.services import ExtractService
from app.extract.infrastructure.adapters.http import TVMazeAPI


class ExtractContainer(containers.DeclarativeContainer):
    """
    Dependency Injection Container for the Extract context.

    This container manages the dependencies required for the Extract context, such as
    the TvMazeAPI and ExtractService.
    """

    tvmaze_api_adapter = providers.Singleton(TVMazeAPI)

    extract_service = providers.Singleton(
        ExtractService,
        extractor_adapter=tvmaze_api_adapter,
    )
