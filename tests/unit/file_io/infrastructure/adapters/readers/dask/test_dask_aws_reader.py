import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from io import BytesIO

from app.file_io.infrastructure.adapters.readers import (
    DaskCSVReaderFromS3,
    DaskParquetReaderFromS3,
)


def test_dask_csv_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a CSV file from S3 using Dask and returns a valid Dask DataFrame."""
    content = "a,b\n5,10\n15,20"
    s3_mock_client.download_string.return_value = content

    reader = DaskCSVReaderFromS3(s3=s3_mock_client)
    df = reader.read("data.csv", bucket="mock-bucket")
    result = df.compute()

    assert result.shape == (2, 2)
    assert result.iloc[1]["b"] == 20


def test_dask_parquet_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a Parquet file from S3 using Dask and returns a valid Dask DataFrame."""
    df_pd = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    table = pa.Table.from_pandas(df_pd)
    buffer = BytesIO()
    pq.write_table(table, buffer)

    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = DaskParquetReaderFromS3(s3=s3_mock_client)
    df = reader.read("data.parquet", bucket="mock-bucket")
    result = df.compute()

    assert result.shape == (2, 2)
    assert result.iloc[0]["y"] == "a"


def test_dask_parquet_reader_from_s3_reads_snappy_correctly(s3_mock_client):
    """Reads a Snappy-compressed Parquet file from S3 using Dask and returns a valid Dask DataFrame."""
    df_pd = pd.DataFrame({"z": [9, 8], "w": ["s", "t"]})
    table = pa.Table.from_pandas(df_pd)
    buffer = BytesIO()
    pq.write_table(table, buffer, compression="snappy")

    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = DaskParquetReaderFromS3(s3=s3_mock_client)
    df = reader.read("compressed.parquet", bucket="mock-bucket")
    result = df.compute()

    assert result.shape == (2, 2)
    assert result.iloc[1]["w"] == "t"
