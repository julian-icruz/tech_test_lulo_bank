import json

from app.file_io.infrastructure.adapters.writers import JSONWriter


def test_write_json_writes_dict_correctly(tmp_path):
    """
    Writes a dictionary to a JSON file and verifies the content matches.
    """
    data = {"name": "Alice", "age": 30}
    path = tmp_path / "dict.json"

    writer = JSONWriter()
    writer.write(data, str(path))

    with open(path, "r", encoding="utf-8") as f:
        result = json.load(f)

    assert result == data


def test_write_json_writes_list_correctly(tmp_path):
    """
    Writes a list of dictionaries to a JSON file and verifies the content matches.
    """
    data = [{"id": 1}, {"id": 2}]
    path = tmp_path / "list.json"

    writer = JSONWriter()
    writer.write(data, str(path))

    with open(path, "r", encoding="utf-8") as f:
        result = json.load(f)

    assert result == data


def test_write_json_with_custom_indent(tmp_path):
    """
    Writes JSON with indentation and checks for expected formatting.
    """
    data = {"x": 100, "y": 200}
    path = tmp_path / "pretty.json"

    writer = JSONWriter()
    writer.write(data, str(path), indent=4)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    assert content.startswith("{\n")
    assert '"x": 100' in content
