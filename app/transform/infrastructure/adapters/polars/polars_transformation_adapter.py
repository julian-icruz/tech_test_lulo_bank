import polars as pl
from typing import Any, List
from dataclasses import dataclass

from app.transform.domain.ports.data_transformation_port import DataTransformationPort


@dataclass
class PolarsTransformation(DataTransformationPort):
    def flatten_nested_structures(self, data: Any) -> Any:
        pass

    def convert_date_time_columns(self, data: Any) -> Any:
        pass

    def normalize_columns(self, data: Any) -> Any:
        pass

    def categorize_columns(self, data: Any) -> Any:
        pass

    def merge_dataframes(self, data_list: List[Any]) -> Any:
        """
        Merges a list of Polars DataFrames into a single DataFrame.

        Args:
            data_list (List[Any]): A list of Polars DataFrame objects.

        Returns:
            Any: A single Polars DataFrame resulting from concatenation.
        """
        if not data_list:
            raise ValueError("No data provided for merging.")
        return pl.concat(data_list)
