from csv import reader
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dict, Factory, Singleton

from app.file_io.infrastructure.clients import S3Adapter

from app.file_io.infrastructure.adapters.readers import (
    # -------------- PANDAS ---------------- #
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
    # -------------- POLARS -----Q----------- #
    PolarsCSVReader,
    PolarsJSONReader,
    PolarsParquetReader,
    PolarsCSVReaderFromS3,
    PolarsParquetReaderFromS3,
    # -------------- DASK ---------------- #
    DaskCSVReader,
    DaskParquetReader,
    DaskCSVReaderFromS3,
    DaskParquetReaderFromS3,
    # -------------- JSON ---------------- #
    JSONReader,
    JSONReaderFromS3,
    # -------------- YAML ---------------- #
    YAMLReader,
    YAMLReaderFromS3,
)

from app.file_io.infrastructure.adapters.writers import (
    # -------------- PANDAS ---------------- #
    PandasCSVWriter,
    PandasJSONWriter,
    PandasParquetWriter,
    PandasCSVWriterToS3,
    PandasJSONWriterToS3,
    PandasParquetWriterToS3,
    # -------------- POLARS ---------------- #
    PolarsCSVWriter,
    PolarsParquetWriter,
    PolarsCSVWriterToS3,
    PolarsParquetWriterToS3,
    # -------------- DASK ---------------- #
    DaskParquetWriter,
    DaskParquetWriterToS3,
    # -------------- JSON ---------------- #
    JSONWriter,
    JSONWriterToS3,
    # -------------- YAML ---------------- #
    YAMLWriter,
    YAMLWriterToS3,
    # -------------- HTML ---------------- #
    HTMLWriter,
    HTMLWriterToS3,
    # -------------- PDF ---------------- #
    PDFKitWriter,
    PDFWriterToS3,
)

from app.file_io.application.services import ReaderWriterSelectorService


class FileIOContainer(DeclarativeContainer):
    """
    Dependency injection container for File I/O adapters (readers & writers).

    This container provides structured access to file readers and writers for different
    formats (CSV, JSON, Parquet, YAML, HTML, PDF) and sources (local filesystem, AWS S3).

    It supports multiple engines (pandas, polars, dask, native libraries like json/yaml)
    and abstracts away S3 logic using a shared singleton S3Adapter.

    ----------------------------
    Structure:
        readers[source][format][engine]
        writers[source][format][engine]

    Where:
        - source: "local" or "aws"
        - format: "csv", "json", "parquet", "yaml", "html", "pdf"
        - engine:
            - For CSV/Parquet/JSON: "pandas", "polars", "dask", or "json"
            - For YAML: "yaml"
            - For HTML: "html"
            - For PDF: "pdfkit", "weasyprint"

    ----------------------------
    Examples:
        >>> reader = container.readers()["aws"]["csv"]["pandas"]
        >>> df = reader.read("data.csv", bucket="my-bucket")

        >>> writer = container.writers()["local"]["pdf"]["weasyprint"]
        >>> writer.write("<h1>Report</h1>", "report.pdf")

        >>> writer = container.writers()["aws"]["json"]["json"]
        >>> writer.write({"name": "J"}, "user.json", bucket="my-bucket")

    ----------------------------
    Notes:
        - All AWS readers and writers require a 'bucket' keyword argument.
        - `s3_adapter` is injected once via Singleton for all AWS dependencies.
        - This structure allows flexible selection and extension of adapters, enabling
          vertical slicing and hexagonal architecture principles.
        - Supports a variety of engines (pandas, polars, dask) for various file formats (CSV,
          JSON, Parquet), as well as libraries such as `json`, `yaml`, `html`, and `pdfkit`.
    """

    s3_adapter = Singleton(S3Adapter)

    local_readers = Dict(
        csv=Dict(
            pandas=Factory(PandasCSVReader),
            polars=Factory(PolarsCSVReader),
            dask=Factory(DaskCSVReader),
        ),
        json=Dict(
            pandas=Factory(PandasJSONReader),
            polars=Factory(PolarsJSONReader),
            json=Factory(JSONReader),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetReader),
            polars=Factory(PolarsParquetReader),
            dask=Factory(DaskParquetReader),
        ),
        yaml=Dict(
            yaml=Factory(YAMLReader),
        ),
    )

    aws_readers = Dict(
        csv=Dict(
            pandas=Factory(PandasCSVReaderFromS3, s3=s3_adapter),
            polars=Factory(PolarsCSVReaderFromS3, s3=s3_adapter),
            dask=Factory(DaskCSVReaderFromS3, s3=s3_adapter),
        ),
        json=Dict(
            pandas=Factory(PandasJSONReaderFromS3, s3=s3_adapter),
            json=Factory(JSONReaderFromS3, s3=s3_adapter),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetReaderFromS3, s3=s3_adapter),
            polars=Factory(PolarsParquetReaderFromS3, s3=s3_adapter),
            dask=Factory(DaskParquetReaderFromS3, s3=s3_adapter),
        ),
        yaml=Dict(
            yaml=Factory(YAMLReaderFromS3, s3=s3_adapter),
        ),
    )

    local_writers = Dict(
        csv=Dict(
            pandas=Factory(PandasCSVWriter),
            polars=Factory(PolarsCSVWriter),
        ),
        json=Dict(
            pandas=Factory(PandasJSONWriter),
            json=Factory(JSONWriter),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetWriter),
            polars=Factory(PolarsParquetWriter),
            dask=Factory(DaskParquetWriter),
        ),
        yaml=Dict(
            yaml=Factory(YAMLWriter),
        ),
        html=Dict(
            html=Factory(HTMLWriter),
        ),
        pdf=Dict(
            pdfkit=Factory(PDFKitWriter),
        ),
    )

    aws_writers = Dict(
        csv=Dict(
            pandas=Factory(PandasCSVWriterToS3, s3=s3_adapter),
            polars=Factory(PolarsCSVWriterToS3, s3=s3_adapter),
        ),
        json=Dict(
            pandas=Factory(PandasJSONWriterToS3, s3=s3_adapter),
            json=Factory(JSONWriterToS3, s3=s3_adapter),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetWriterToS3, s3=s3_adapter),
            polars=Factory(PolarsParquetWriterToS3, s3=s3_adapter),
            dask=Factory(DaskParquetWriterToS3, s3=s3_adapter),
        ),
        yaml=Dict(
            yaml=Factory(YAMLWriterToS3, s3=s3_adapter),
        ),
        html=Dict(
            html=Factory(HTMLWriterToS3, s3=s3_adapter),
        ),
        pdf=Dict(
            pdf=Factory(PDFWriterToS3, s3=s3_adapter),
        ),
    )

    readers = Dict(
        local=local_readers,
        aws=aws_readers,
    )
    writers = Dict(
        local=local_writers,
        aws=aws_writers,
    )

    reader_writer_selector_service = Factory(
        ReaderWriterSelectorService,
        reader_factory=readers,
        writer_factory=writers,
    )
