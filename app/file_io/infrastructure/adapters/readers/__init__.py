from app.file_io.infrastructure.adapters.readers.base.s3_reader import BaseS3Reader

# ------------------------------- PANDAS ------------------------------- #
from app.file_io.infrastructure.adapters.readers.pandas.csv_reader import (
    PandasCSVReader,
)
from app.file_io.infrastructure.adapters.readers.pandas.json_reader import (
    PandasJSONReader,
)
from app.file_io.infrastructure.adapters.readers.pandas.parquet_reader import (
    PandasParquetReader,
)
from app.file_io.infrastructure.adapters.readers.pandas.aws_reader import (
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
)

# ------------------------------- POLARS ------------------------------- #
from app.file_io.infrastructure.adapters.readers.polars.csv_reader import (
    PolarsCSVReader,
)
from app.file_io.infrastructure.adapters.readers.polars.json_reader import (
    PolarsJSONReader,
)
from app.file_io.infrastructure.adapters.readers.polars.parquet_reader import (
    PolarsParquetReader,
)
from app.file_io.infrastructure.adapters.readers.polars.aws_reader import (
    PolarsCSVReaderFromS3,
    PolarsParquetReaderFromS3,
)

# ------------------------------- DASK ------------------------------- #
from app.file_io.infrastructure.adapters.readers.dask.csv_reader import DaskCSVReader
from app.file_io.infrastructure.adapters.readers.dask.parquet_reader import (
    DaskParquetReader,
)
from app.file_io.infrastructure.adapters.readers.dask.aws_reader import (
    DaskCSVReaderFromS3,
    DaskParquetReaderFromS3,
)

# ------------------------------- JSON ------------------------------- #
from app.file_io.infrastructure.adapters.readers.json.json_reader import JSONReader
from app.file_io.infrastructure.adapters.readers.json.aws_reader import JSONReaderFromS3

# ------------------------------- YAML ------------------------------- #
from app.file_io.infrastructure.adapters.readers.yaml.yaml_reader import YAMLReader
from app.file_io.infrastructure.adapters.readers.yaml.aws_reader import YAMLReaderFromS3

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
    PolarsJSONReader,
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
