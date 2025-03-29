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
def json_file_path():
    """
    Fixture that creates a temporary JSON file and returns its path.
    """
    content = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        f.write(content)
        f.seek(0)
        yield f.name
