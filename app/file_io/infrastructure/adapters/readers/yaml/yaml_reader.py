import yaml
from typing import Any
from file_io.domain.ports.file_reader import FileReader


class YAMLReader(FileReader):
    """
    Reads a YAML file using PyYAML.

    Args:
        path (str): The path to the YAML file.
        **kwargs: Optional parameters passed to yaml.safe_load() (e.g., encoding).

    Returns:
        Any: Parsed YAML content as a dict, list, or other compatible object.
    """

    def read(self, path: str, **kwargs) -> Any:
        encoding = kwargs.get("encoding", "utf-8")
        with open(path, "r", encoding=encoding) as f:
            return yaml.safe_load(f)
