from file_io.infrastructure.adapters.readers.pandas.csv_reader import PandasCSVReader
from file_io.infrastructure.adapters.readers.pandas.json_reader import PandasJSONReader
from file_io.infrastructure.adapters.readers.pandas.parquet_reader import (
    PandasParquetReader,
)

from file_io.infrastructure.adapters.readers.polars.csv_reader import PolarsCSVReader
from file_io.infrastructure.adapters.readers.polars.parquet_reader import (
    PolarsParquetReader,
)

PARQUET_READERS = [
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
]

POLARS_RESDERS = [
    PolarsCSVReader,
    PolarsParquetReader,
]

__ALL__ = [
    PARQUET_READERS,
    POLARS_RESDERS,
]
