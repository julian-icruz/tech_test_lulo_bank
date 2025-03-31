from dataclasses import dataclass

from typing import Any, Dict
from app.transform.domain.ports import DataProfilingPort, DataTransformationPort


@dataclass
class ProfilingService:
    profiling_adapters: dict[str, DataProfilingPort]
    transformation_adapters: dict[str, DataTransformationPort]
    profiling_adapter: DataProfilingPort = None
    transformation_adapter: DataTransformationPort = None

    def _select_adapter(self, key: str) -> None:
        """
        Selects the appropriate profiling and transformation adapters based on the provided key.

        Args:
            key (str): The key identifying the adapter to use.

        Raises:
            ValueError: If the key is not found in either the profiling_adapters or transformation_adapters dictionaries.
        """
        try:
            self.profiling_adapter = self.profiling_adapters[key]
            self.transformation_adapter = self.transformation_adapters[key]
        except KeyError as e:
            raise ValueError(
                f"Adapter key '{key}' not found in the adapter dictionaries."
            ) from e

    def __call__(self, data: Any) -> Dict[str, Any]:
        """
        Orchestrates the data profiling process by invoking methods from the data profiling adapter.

        Args:
            data (Any): Input data (e.g., a DataFrame from pandas, polars, or dask).

        Returns:
            Dict[str, Any]: A dictionary containing profiling results including descriptive statistics,
                            missing values, duplicates, correlations, and column type profiles.
        """
        results = {}
        data_flattened = []
        for df in data:
            data_flattened.append(
                self.transformation_adapter.flatten_nested_structures(df)
            )
        data = self.transformation_adapter.merge_dataframes(data_flattened)
        results["descriptive_statistics"] = (
            self.profiling_adapter.generate_descriptive_statistics(data)
        )
        results["missing_values"] = self.profiling_adapter.detect_missing_values(data)
        results["duplicates"] = self.profiling_adapter.detect_duplicates(data)
        results["correlations"] = self.profiling_adapter.compute_correlations(data)
        results["column_types"] = self.profiling_adapter.profile_column_types(data)
        return results
