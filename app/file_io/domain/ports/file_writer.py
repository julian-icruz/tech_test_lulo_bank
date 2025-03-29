from typing import Any
from abc import ABC, abstractmethod


class FileWriter(ABC):
    @abstractmethod
    def write(self, data: Any, path: str, **kwargs):
        """
        Write the provided data to the given file path.
        Format and encoding depend on the implementation.

        Args:
            data (Any): Data to be written (commonly a DataFrame or list of dicts).
            path (str): Path or destination URI to write the file to.
        """
        pass
