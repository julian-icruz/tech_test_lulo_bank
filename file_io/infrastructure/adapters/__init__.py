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

from file_io.infrastructure.adapters.readers.structured.json_reader import JSONReader
from file_io.infrastructure.adapters.readers.structured.yaml_reader import YAMLReader

from file_io.infrastructure.adapters.readers.aws.s3_text_reader import S3TextReader
from file_io.infrastructure.adapters.readers.aws.s3_binary_reader import S3BinaryReader


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

STRUCTURED_READERS = [
    JSONReader,
    YAMLReader,
]

AWS_READERS = [
    S3TextReader,
    S3BinaryReader,
]

READERS = [
    PARQUET_READERS,
    POLARS_RESDERS,
    DASK_READERS,
]

__ALL__ = [
    READERS,
]
