import pytest
import tempfile


@pytest.fixture
def temp_csv_path():
    """Creates a temporary CSV file with given content and returns its file path."""

    def _create(content: str):
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
            f.write(content)
            return f.name

    return _create


@pytest.fixture
def temp_json_path():
    """Creates a temporary JSON file with given content and returns its file path."""

    def _create(content: str):
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
            f.write(content)
            return f.name

    return _create
