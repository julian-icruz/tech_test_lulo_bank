from file_io.infrastructure.adapters.readers.base.s3_reader import BaseS3Reader

# ------------------------------- PANDAS ------------------------------- #
from file_io.infrastructure.adapters.readers.pandas.csv_reader import PandasCSVReader
from file_io.infrastructure.adapters.readers.pandas.json_reader import PandasJSONReader
from file_io.infrastructure.adapters.readers.pandas.parquet_reader import (
    PandasParquetReader,
)
from file_io.infrastructure.adapters.readers.pandas.aws_reader import (
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
)

# ------------------------------- POLARS ------------------------------- #
from file_io.infrastructure.adapters.readers.polars.csv_reader import PolarsCSVReader
from file_io.infrastructure.adapters.readers.polars.parquet_reader import (
    PolarsParquetReader,
)
from file_io.infrastructure.adapters.readers.polars.aws_reader import (
    PolarsCSVReaderFromS3,
    PolarsParquetReaderFromS3,
)

# ------------------------------- DASK ------------------------------- #
from file_io.infrastructure.adapters.readers.dask.csv_reader import DaskCSVReader
from file_io.infrastructure.adapters.readers.dask.parquet_reader import (
    DaskParquetReader,
)
from file_io.infrastructure.adapters.readers.dask.aws_reader import (
    DaskCSVReaderFromS3,
    DaskParquetReaderFromS3,
)

# ------------------------------- JSON ------------------------------- #
from file_io.infrastructure.adapters.readers.json.json_reader import JSONReader
from file_io.infrastructure.adapters.readers.json.aws_reader import JSONReaderFromS3

# ------------------------------- YAML ------------------------------- #
from file_io.infrastructure.adapters.readers.yaml.yaml_reader import YAMLReader
from file_io.infrastructure.adapters.readers.yaml.aws_reader import YAMLReaderFromS3

BASE_READERS = [
    BaseS3Reader,
]

PANDAS_READERS = [
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
]

POLARS_RESDERS = [
    PolarsCSVReader,
    PolarsParquetReader,
    PolarsCSVReaderFromS3,
    PolarsParquetReaderFromS3,
]

DASK_READERS = [
    DaskCSVReader,
    DaskParquetReader,
    DaskCSVReaderFromS3,
    DaskParquetReaderFromS3,
]

JSON_READERS = [
    JSONReader,
    JSONReaderFromS3,
]

YAML_READERS = [
    YAMLReader,
    YAMLReaderFromS3,
]

READERS = [
    BASE_READERS,
    PANDAS_READERS,
    POLARS_RESDERS,
    DASK_READERS,
    JSON_READERS,
    YAML_READERS,
]

__ALL__ = [
    READERS,
]
