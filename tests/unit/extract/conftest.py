import pytest

from app.extract import ExtractContainer
from app.extract.infrastructure.adapters.http import TVMazeAPIAdapter


@pytest.fixture
def tvmaze_api_adapter():
    return TVMazeAPIAdapter()


@pytest.fixture
def extract_container():
    """
    Fixture that initializes and wires the ExtractContainer.
    """
    container = ExtractContainer()
    container.init_resources()
    container.wire(modules=[__name__])
    return container
