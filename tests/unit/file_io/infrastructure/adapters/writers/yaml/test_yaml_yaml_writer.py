import yaml
from app.file_io.infrastructure.adapters.writers import YAMLWriter


def test_yaml_writer_writes_dict(tmp_path):
    """
    Writes a dictionary to a YAML file and verifies the parsed content matches.
    """
    data = {"framework": "FastAPI", "language": "Python"}
    path = tmp_path / "test.yaml"

    writer = YAMLWriter()
    writer.write(data, str(path))

    with open(path, "r", encoding="utf-8") as f:
        result = yaml.safe_load(f)

    assert result == data


def test_yaml_writer_writes_list(tmp_path):
    """
    Writes a list to a YAML file and checks the parsed structure.
    """
    data = ["red", "green", "blue"]
    path = tmp_path / "colors.yaml"

    writer = YAMLWriter()
    writer.write(data, str(path))

    with open(path, "r", encoding="utf-8") as f:
        result = yaml.safe_load(f)

    assert result == data


def test_yaml_writer_with_custom_encoding(tmp_path):
    """
    Writes YAML with a custom encoding (e.g., UTF-8) and reads it back.
    """
    data = {"emoji": "😀"}
    path = tmp_path / "emoji.yaml"

    writer = YAMLWriter()
    writer.write(data, str(path), encoding="utf-8")

    with open(path, "r", encoding="utf-8") as f:
        result = yaml.safe_load(f)

    assert result["emoji"] == "😀"
