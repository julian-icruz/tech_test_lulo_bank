from app.extract.domain.services import ExtractService
from app.extract.infrastructure.adapters.http import TVMazeAPIAdapter


def test_extract_service_instantiation(extract_container):
    """
    Tests that the extract_service provider returns an instance of ExtractService
    and its extractor_adapter is an instance of TVMazeAPIAdapter.
    """
    service = extract_container.extract_service()
    assert isinstance(service, ExtractService)
    assert isinstance(service.extractor_adapter, TVMazeAPIAdapter)


def test_extract_service_singleton(extract_container):
    """
    Tests that the extract_service provider behaves as a singleton.
    """
    service1 = extract_container.extract_service()
    service2 = extract_container.extract_service()
    assert service1 is service2
