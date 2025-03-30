import pytest
import yaml
import tempfile


from app.file_io.infrastructure.adapters.readers import YAMLReader


def test_read_valid_yaml_file(temp_yaml_path):
    """Reads a valid YAML file and checks the returned dictionary."""
    content = """
    name: Julian
    skills:
      - python
      - fastapi
    """
    path = temp_yaml_path(content)
    reader = YAMLReader()
    result = reader.read(path)

    assert isinstance(result, dict)
    assert result["name"] == "Julian"
    assert "python" in result["skills"]


def test_read_yaml_list():
    """Reads a YAML list and checks the returned structure."""
    content = """
    - apple
    - banana
    - cherry
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".yaml", delete=False) as f:
        f.write(content)
        path = f.name

    reader = YAMLReader()
    result = reader.read(path)

    assert isinstance(result, list)
    assert result[1] == "banana"


def test_read_invalid_yaml_file():
    """Checks that invalid YAML raises a YAMLError."""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".yaml", delete=False) as f:
        f.write("{not: valid: yaml")
        path = f.name

    reader = YAMLReader()
    with pytest.raises(yaml.YAMLError):
        reader.read(path)


def test_read_nonexistent_yaml_file():
    """Checks that reading a non-existent YAML file raises FileNotFoundError."""
    reader = YAMLReader()
    with pytest.raises(FileNotFoundError):
        reader.read("missing.yaml")
