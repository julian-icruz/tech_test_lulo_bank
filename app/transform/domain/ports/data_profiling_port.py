from typing import Any, Dict
from abc import ABC, abstractmethod


class DataProfilingPort(ABC):
    @abstractmethod
    def generate_descriptive_statistics(self, data: Any) -> Dict[str, Any]:
        """
        Generates descriptive statistics (mean, median, standard deviation, etc.) for numerical columns.

        Args:
            data (Any): DataFrame from pandas, polars, or dask.

        Returns:
            Dict[str, Any]: Descriptive statistics for each column.
        """
        pass

    @abstractmethod
    def detect_missing_values(self, data: Any) -> Dict[str, Any]:
        """
        Detects and summarizes missing values in the dataset.

        Args:
            data (Any): DataFrame from pandas, polars, or dask.

        Returns:
            Dict[str, Any]: Information on the count and proportion of missing values.
        """
        pass

    @abstractmethod
    def detect_duplicates(self, data: Any) -> Dict[str, Any]:
        """
        Identifies duplicate records in the dataset.

        Args:
            data (Any): DataFrame from pandas, polars, or dask.

        Returns:
            Dict[str, Any]: Summary of duplicate records.
        """
        pass

    @abstractmethod
    def compute_correlations(self, data: Any) -> Dict[str, Any]:
        """
        Computes correlations between numerical variables.

        Args:
            data (Any): DataFrame from pandas, polars, or dask.

        Returns:
            Dict[str, Any]: Correlation matrix or summary.
        """
        pass

    @abstractmethod
    def profile_column_types(self, data: Any) -> Dict[str, Any]:
        """
        Determines and summarizes the data types (numeric, categorical, date, etc.) of each column.

        Args:
            data (Any): DataFrame from pandas, polars, or dask.

        Returns:
            Dict[str, Any]: Summary of data types per column.
        """
        pass
