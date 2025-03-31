import pandas as pd
from typing import Any, List
from dataclasses import dataclass

from app.transform.domain.ports.data_transformation_port import DataTransformationPort


@dataclass
class PandasTransformation(DataTransformationPort):
    def flatten_nested_structures(self, data: Any) -> Any:
        return pd.json_normalize(data["_embedded"]["show"])

    def convert_date_time_columns(self, data: Any) -> Any:
        pass

    def normalize_columns(self, data: Any) -> Any:
        pass

    def categorize_columns(self, data: Any) -> Any:
        pass

    def merge_dataframes(self, data_list: List[Any]) -> Any:
        """
        Merges a list of pandas DataFrames into a single DataFrame.

        Args:
            data_list (List[Any]): A list of pandas DataFrame objects.

        Returns:
            Any: A single pandas DataFrame resulting from concatenation.
        """
        if not data_list:
            raise ValueError("No data provided for merging.")
        return pd.concat(data_list, ignore_index=True)
