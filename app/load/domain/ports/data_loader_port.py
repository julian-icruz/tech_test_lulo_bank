from abc import ABC, abstractmethod


class DataLoaderPort(ABC):
    @abstractmethod
    def load_data(self, data: list[dict]) -> None:
        """
        Loads data into the database.

        Args:
            data (list[dict]): List of records (dictionaries) to insert.
        """
        pass
