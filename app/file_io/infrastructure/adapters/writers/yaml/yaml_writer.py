import yaml
from typing import Any
from app.file_io.domain.ports import FileWriter


class YAMLWriter(FileWriter):
    """
    Writes a Python object (dict, list, etc.) to a local YAML file
    using PyYAML.

    Args:
        data (Any): The object to serialize.
        path (str): The path to save the YAML file.
        **kwargs: Additional arguments for yaml.dump().
    """

    def write(self, data: Any, path: str, **kwargs) -> None:
        encoding = kwargs.pop("encoding", "utf-8")
        with open(path, "w", encoding=encoding) as f:
            yaml.safe_dump(data, f, **kwargs)
