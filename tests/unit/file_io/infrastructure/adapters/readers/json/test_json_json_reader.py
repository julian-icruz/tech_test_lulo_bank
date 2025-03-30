import pytest
import json

from app.file_io.infrastructure.adapters.readers import JSONReader


def test_read_valid_json_file(tmp_path):
    """Reads a valid JSON file and checks the returned dictionary."""
    content = {"name": "Julian", "age": 30}
    path = tmp_path / "test.json"
    path.write_text(json.dumps(content))

    reader = JSONReader()
    result = reader.read(str(path))

    assert isinstance(result, dict)
    assert result["name"] == "Julian"
    assert result["age"] == 30


def test_read_json_array(tmp_path):
    """Reads a JSON array and checks the returned list."""
    content = [{"a": 1}, {"a": 2}]
    path = tmp_path / "array.json"
    path.write_text(json.dumps(content))

    reader = JSONReader()
    result = reader.read(str(path))

    assert isinstance(result, list)
    assert result[1]["a"] == 2


def test_read_invalid_json(tmp_path):
    """Checks that an invalid JSON file raises a JSONDecodeError."""
    path = tmp_path / "invalid.json"
    path.write_text("{ invalid json }")

    reader = JSONReader()
    with pytest.raises(json.JSONDecodeError):
        reader.read(str(path))


def test_read_nonexistent_json():
    """Checks that reading a missing file raises FileNotFoundError."""
    reader = JSONReader()
    with pytest.raises(FileNotFoundError):
        reader.read("no_such_file.json")
