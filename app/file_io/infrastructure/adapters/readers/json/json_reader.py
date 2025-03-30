import json
from typing import Any
from app.file_io.domain.ports.file_reader import FileReader


class JSONReader(FileReader):
    """
    Reads a JSON file using Python's built-in json module.

    Args:
        path (str): The path to the JSON file.
        **kwargs: Optional parameters passed to json.load() (e.g., encoding).

    Returns:
        Any: Parsed JSON content as a dict, list, or other JSON-compatible object.
    """

    def read(self, path: str, **kwargs) -> Any:
        encoding = kwargs.get("encoding", "utf-8")
        with open(path, "r", encoding=encoding) as f:
            return json.load(f)
