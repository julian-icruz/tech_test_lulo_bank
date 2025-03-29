import json
from typing import Any
from file_io.domain.ports import FileWriter


class JSONWriter(FileWriter):
    """
    Writes a Python object (dict, list, etc.) to a local JSON file
    using Python's built-in json module.

    Args:
        data (Any): The object to serialize.
        path (str): The path to save the JSON file.
        **kwargs: Additional arguments for json.dump().
    """

    def write(self, data: Any, path: str, **kwargs) -> None:
        encoding = kwargs.pop("encoding", "utf-8")
        with open(path, "w", encoding=encoding) as f:
            json.dump(data, f, **kwargs)
