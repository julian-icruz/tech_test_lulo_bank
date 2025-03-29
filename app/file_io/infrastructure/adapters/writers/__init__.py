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

# ------------------------------- YAML ------------------------------- #
from file_io.infrastructure.adapters.writers.yaml.yaml_writer import YAMLWriter
from file_io.infrastructure.adapters.writers.yaml.aws_writer import (
    YAMLWriterToS3,
)

# ------------------------------- HTML ------------------------------- #
from file_io.infrastructure.adapters.writers.html.html_writer import HTMLWriter
from file_io.infrastructure.adapters.writers.html.aws_writer import HTMLWriterToS3


# ------------------------------- PDF ------------------------------- #
from file_io.infrastructure.adapters.writers.pdf.pdfkit_writer import PDFKitWriter
from file_io.infrastructure.adapters.writers.pdf.aws_writer import PDFWriterToS3

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

YAML_WRITERS = [
    YAMLWriter,
    YAMLWriterToS3,
]

HTML_WRITERS = [
    HTMLWriter,
    HTMLWriterToS3,
]

PDF_WRITERS = [
    PDFKitWriter,
    PDFWriterToS3,
]

__ALL__ = [
    BASE_WRITERS,
    PANDAS_WRITERS,
    POLARS_WRITERS,
    JSON_WRITERS,
    YAML_WRITERS,
    HTML_WRITERS,
    PDF_WRITERS,
]
