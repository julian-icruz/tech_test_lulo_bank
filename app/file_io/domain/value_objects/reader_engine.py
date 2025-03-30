from enum import Enum


class ReaderEngine(str, Enum):
    PANDAS = "pandas"
    POLARS = "polars"
    DASK = "dask"
    JSON = "json"
    YAML = "yaml"
