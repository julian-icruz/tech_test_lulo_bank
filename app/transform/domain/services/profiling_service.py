from typing import Any


from app.transform.domain.services import BaseTransformService


class ProfilingService(BaseTransformService):

    def __call__(self, data: Any) -> dict[str, Any]:
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
