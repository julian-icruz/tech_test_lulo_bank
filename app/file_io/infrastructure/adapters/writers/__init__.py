from file_io.infrastructure.adapters.writers.base.s3_writer import BaseS3Writer

# ------------------------------- PANDAS ------------------------------- #
from file_io.infrastructure.adapters.writers.pandas.csv_writer import PandasCSVWriter
from file_io.infrastructure.adapters.writers.pandas.json_writer import PandasJSONWriter
from file_io.infrastructure.adapters.writers.pandas.parquet_writer import (
    PandasParquetWriter,
)
from file_io.infrastructure.adapters.writers.pandas.aws_writer import (
    PandasCSVWriterToS3,
    PandasJSONWriterToS3,
    PandasParquetWriterToS3,
)

# ------------------------------- POLARS ------------------------------- #
from file_io.infrastructure.adapters.writers.polars.csv_writer import PolarsCSVWriter
from file_io.infrastructure.adapters.writers.polars.parquet_writer import (
    PolarsParquetWriter,
)
from file_io.infrastructure.adapters.writers.polars.aws_writer import (
    PolarsCSVWriterToS3,
    PolarsParquetWriterToS3,
)

# -------------------------------- JSON ------------------------------- #
from file_io.infrastructure.adapters.writers.json.json_writer import JSONWriter
from file_io.infrastructure.adapters.writers.json.aws_writer import (
    JSONWriterToS3,
)

BASE_WRITERS = [
    BaseS3Writer,
]

PANDAS_WRITERS = [
    PandasCSVWriter,
    PandasJSONWriter,
    PandasParquetWriter,
    PandasCSVWriterToS3,
    PandasJSONWriterToS3,
    PandasParquetWriterToS3,
]

POLARS_WRITERS = [
    PolarsCSVWriter,
    PolarsParquetWriter,
    PolarsCSVWriterToS3,
    PolarsParquetWriterToS3,
]

JSON_WRITERS = [
    JSONWriter,
    JSONWriterToS3,
]

__ALL__ = [
    BASE_WRITERS,
    PANDAS_WRITERS,
    POLARS_WRITERS,
    JSON_WRITERS,
]
