from typing import Any

from app.transform.domain.services import BaseTransformService


class DataCleaningService(BaseTransformService):

    def __call__(self, data: Any) -> dict[str, Any]:
        """
        Orchestrates the data profiling process by invoking methods from the data profiling adapter.

        Args:
            data (Any): Input data (e.g., a DataFrame from pandas, polars, or dask).

        Returns:
            Dict[str, Any]: A dictionary containing profiling results including descriptive statistics,
                            missing values, duplicates, correlations, and column type profiles.
        """
        data_flattened = []
        for df in data:
            data_flattened.append(
                self.transformation_adapter.flatten_nested_structures(df)
            )

        return data_flattened.shape
