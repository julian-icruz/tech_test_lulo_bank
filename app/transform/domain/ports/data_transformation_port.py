from typing import Any, List
from abc import ABC, abstractmethod


class DataTransformationPort(ABC):
    @abstractmethod
    def flatten_nested_structures(self, data: Any) -> Any:
        """
        Flattens nested data structures present in the input data.

        Args:
            data (Any): The input data, typically a DataFrame or similar structure.

        Returns:
            Any: The data with nested structures flattened.
        """
        pass

    @abstractmethod
    def convert_date_time_columns(self, data: Any) -> Any:
        """
        Converts date/time columns in the input data to a standardized format.

        Args:
            data (Any): The input data containing date/time columns.

        Returns:
            Any: The data with date/time columns converted to a uniform format.
        """
        pass

    @abstractmethod
    def normalize_columns(self, data: Any) -> Any:
        """
        Normalizes numerical columns in the input data.

        Args:
            data (Any): The input data with numerical columns.

        Returns:
            Any: The data with normalized numerical columns.
        """
        pass

    @abstractmethod
    def categorize_columns(self, data: Any) -> Any:
        """
        Categorizes columns in the input data, such as binning numerical values into categorical ranges.

        Args:
            data (Any): The input data.

        Returns:
            Any: The data with columns categorized.
        """
        pass

    @abstractmethod
    def merge_dataframes(self, data_list: List[Any]) -> Any:
        """
        Merges a list of DataFrame objects into a single consolidated DataFrame.

        Args:
            data_list (List[Any]): A list of data objects (e.g., DataFrames) to be merged.

        Returns:
            Any: The merged data.
        """
        pass
