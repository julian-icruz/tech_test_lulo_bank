from file_io.infrastructure.adapters.readers.pandas.csv_reader import PandasCSVReader
from file_io.infrastructure.adapters.readers.pandas.json_reader import PandasJSONReader
from file_io.infrastructure.adapters.readers.pandas.parquet_reader import (
    PandasParquetReader,
)

from file_io.infrastructure.adapters.readers.polars.csv_reader import PolarsCSVReader
from file_io.infrastructure.adapters.readers.polars.parquet_reader import (
    PolarsParquetReader,
)

from file_io.infrastructure.adapters.readers.dask.csv_reader import DaskCSVReader
from file_io.infrastructure.adapters.readers.dask.parquet_reader import (
    DaskParquetReader,
)

from file_io.infrastructure.adapters.readers.json.json_reader import JSONReader

from file_io.infrastructure.adapters.readers.yaml.yaml_reader import YAMLReader

PARQUET_READERS = [
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
]

POLARS_RESDERS = [
    PolarsCSVReader,
    PolarsParquetReader,
]

DASK_READERS = [
    DaskCSVReader,
    DaskParquetReader,
]

JSON_READERS = [
    JSONReader,
]

YAML_READERS = [
    YAMLReader,
]

READERS = [
    PARQUET_READERS,
    POLARS_RESDERS,
    DASK_READERS,
    JSON_READERS,
    YAML_READERS,
]

__ALL__ = [
    READERS,
]
