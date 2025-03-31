from dataclasses import dataclass

from app.transform.domain.ports import DataProfilingPort, DataTransformationPort


@dataclass
class BaseTransformService:
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
