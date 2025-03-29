from file_io.infrastructure.adapters.writers.base.s3_writer import BaseS3Writer

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

__ALL__ = [
    BASE_WRITERS,
    PANDAS_WRITERS,
]
