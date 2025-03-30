import pytest

from app.extract.infrastructure.adapters.http import TVMazeAPIAdapter


@pytest.fixture
def tvmaze_api_adapter():
    return TVMazeAPIAdapter()
