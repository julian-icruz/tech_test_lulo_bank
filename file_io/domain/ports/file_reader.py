from typing import Any
from abc import ABC, abstractmethod


class FileReader(ABC):
    @abstractmethod
    def read(self, path: str) -> Any:
        """
        Read a file from the given path and return its contents.
        The format of the returned data depends on the implementation.

        Args:
            path (str): Path to the input file (local or remote).

        Returns:
            Any: Parsed data (commonly a DataFrame or a list of dicts).
        """
        pass
