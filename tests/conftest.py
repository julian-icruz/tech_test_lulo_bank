import pytest
import tempfile


@pytest.fixture
def csv_file_path():
    """Fixture that creates a temporary CSV file and returns its file path."""
    content = "id,name\n1,Alice\n2,Bob"
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
        f.write(content)
        f.seek(0)
        yield f.name
