from typing import Any
from abc import ABC, abstractmethod


class FileReader(ABC):
    @abstractmethod
    def read(self, path: str, **kwargs) -> Any:
        """
        Read a file from the given path and return its contents.
        Additional format-specific options can be passed as keyword arguments.

        Args:
            path (str): Path to the input file (local or remote).
            **kwargs: Additional parameters for the specific file format.

        Returns:
            Any: Parsed data (commonly a DataFrame or a list of dicts).
        """
        pass
