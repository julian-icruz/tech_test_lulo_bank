import pytest
import tempfile


@pytest.fixture
def csv_file_path():
    """Fixture que crea un archivo CSV temporal y devuelve su path."""
    content = "id,name\n1,Alice\n2,Bob"
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
        f.write(content)
        f.seek(0)
        yield f.name
