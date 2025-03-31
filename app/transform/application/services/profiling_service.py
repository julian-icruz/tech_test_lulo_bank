from dataclasses import dataclass

from typing import Any, Dict
from app.transform.domain.ports import DataProfilingPort


@dataclass
class ProfilingService:
    profiling_adapters: dict[str, DataProfilingPort]
    profiling_adapter: DataProfilingPort = None

    def _select_adapter(self, key: str) -> None:
        """
        Selects the appropriate profiling adapter from the available adapters using the provided key.

        Args:
            key (str): The key identifying the profiling adapter to use.

        Raises:
            ValueError: If the key is not found in the profiling_adapters dictionary.
        """
        if key not in self.profiling_adapters:
            raise ValueError(
                f"Adapter key '{key}' not found in available profiling adapters."
            )
        self.profiling_adapter = self.profiling_adapters[key]

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
        results["descriptive_statistics"] = (
            self.profiling_adapter.generate_descriptive_statistics(data)
        )
        results["missing_values"] = self.profiling_adapter.detect_missing_values(data)
        results["duplicates"] = self.profiling_adapter.detect_duplicates(data)
        results["correlations"] = self.profiling_adapter.compute_correlations(data)
        results["column_types"] = self.profiling_adapter.profile_column_types(data)
        return results
