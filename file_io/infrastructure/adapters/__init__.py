from file_io.infrastructure.adapters.readers.pandas.csv_reader import PandasCSVReader
from file_io.infrastructure.adapters.readers.pandas.json_reader import PandasJSONReader
from file_io.infrastructure.adapters.readers.pandas.parquet_reader import (
    PandasParquetReader,
)

READERS = [
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
]

__ALL__ = [
    READERS,
]
