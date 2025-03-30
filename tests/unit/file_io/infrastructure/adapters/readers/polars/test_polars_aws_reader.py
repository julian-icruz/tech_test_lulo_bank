import polars as pl
from io import BytesIO

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from app.file_io.infrastructure.adapters.readers import (
    PolarsCSVReaderFromS3,
    PolarsParquetReaderFromS3,
)


def test_polars_csv_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a CSV file from mocked S3 using Polars and returns a valid DataFrame."""
    content = "a,b\n1,2\n3,4"
    s3_mock_client.download_string.return_value = content

    reader = PolarsCSVReaderFromS3(s3=s3_mock_client)
    df = reader.read("data/test.csv", bucket="mock-bucket")

    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[0, "a"] == 1


def test_polars_parquet_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a Parquet file from mocked S3 using Polars and returns a valid DataFrame."""

    df_pd = pd.DataFrame({"k": [100, 200], "v": ["foo", "bar"]})
    table = pa.Table.from_pandas(df_pd)
    buffer = BytesIO()
    pq.write_table(table, buffer)
    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = PolarsParquetReaderFromS3(s3=s3_mock_client)
    df = reader.read("data/test.parquet", bucket="mock-bucket")

    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[1, "v"] == "bar"


def test_polars_parquet_reader_from_s3_reads_snappy_correctly(s3_mock_client):
    """Reads a Snappy-compressed Parquet file from mocked S3 using Polars and returns a valid DataFrame."""
    df_pd = pd.DataFrame({"id": [1, 2], "value": ["x", "y"]})
    table = pa.Table.from_pandas(df_pd)

    buffer = BytesIO()
    pq.write_table(table, buffer, compression="snappy")
    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = PolarsParquetReaderFromS3(s3=s3_mock_client)
    df = reader.read("data/snappy_test.parquet", bucket="mock-bucket")

    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[0, "value"] == "x"
