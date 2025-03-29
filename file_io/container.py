from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dict, Factory, Singleton

from file_io.infrastructure.clients import S3Adapter
from file_io.infrastructure.adapters.readers import (
    # -------------- PANDAS ---------------- #
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
    # -------------- POLARS -----Q----------- #
    PolarsCSVReader,
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


class FileIOContainer(DeclarativeContainer):
    """
    Dependency injection container for all file readers (local and AWS).

    This container organizes and provides factory instances for different
    types of file readers based on the data source (local or AWS),
    file format (CSV, JSON, Parquet, YAML), and the parsing engine
    (pandas, polars, dask, or native loaders).

    Structure:
        readers[source][format][engine]

    Where:
        - source: "local" or "aws"
        - format: "csv", "json", "parquet", "yaml"
        - engine: "pandas", "polars", "dask", or "structured" (native parsers)

    Examples:
        >>> reader = container.readers()["aws"]["csv"]["pandas"]
        >>> df = reader.read("path/to/file.csv", bucket="my-bucket")

        >>> reader = container.readers()["local"]["yaml"]["pandas"]
        >>> config = reader.read("config.yaml")

    Notes:
        - All AWS readers require the 'bucket' parameter to be passed via kwargs.
        - S3 readers share a singleton S3Adapter instance.
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
            structured=Factory(JSONReader),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetReader),
            polars=Factory(PolarsParquetReader),
            dask=Factory(DaskParquetReader),
        ),
        yaml=Dict(
            pandas=Factory(YAMLReader),
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
            structured=Factory(JSONReaderFromS3, s3=s3_adapter),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetReaderFromS3, s3=s3_adapter),
            polars=Factory(PolarsParquetReaderFromS3, s3=s3_adapter),
            dask=Factory(DaskParquetReaderFromS3, s3=s3_adapter),
        ),
        yaml=Dict(
            pandas=Factory(YAMLReaderFromS3, s3=s3_adapter),
        ),
    )

    readers = Dict(
        local=local_readers,
        aws=aws_readers,
    )
