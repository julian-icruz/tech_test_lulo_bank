import polars as pl


from app.file_io.infrastructure.adapters.writers import (
    PolarsCSVWriterToS3,
    PolarsParquetWriterToS3,
)


def test_write_polars_csv_to_s3_calls_upload_string(s3_mock_client):
    """
    Verifies that PolarsCSVWriterToS3 correctly serializes and uploads CSV to S3.
    """
    df = pl.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    writer = PolarsCSVWriterToS3(s3=s3_mock_client)

    writer.write(df, "path/file.csv", bucket="my-bucket")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert args[0] == "my-bucket"
    assert args[1] == "path/file.csv"
    assert "a,b" in args[2]  # CSV content


def test_write_polars_parquet_to_s3_calls_upload_bytes(s3_mock_client):
    """
    Verifies that PolarsParquetWriterToS3 correctly serializes and uploads Parquet to S3.
    """
    df = pl.DataFrame({"id": [100, 200], "value": ["foo", "bar"]})
    writer = PolarsParquetWriterToS3(s3=s3_mock_client)

    writer.write(df, "data/output.parquet", bucket="bucket-123")

    s3_mock_client.upload_bytes.assert_called_once()
    args = s3_mock_client.upload_bytes.call_args[0]
    assert args[0] == "bucket-123"
    assert args[1] == "data/output.parquet"
    assert isinstance(args[2], bytes)
    assert len(args[2]) > 0


def test_write_polars_parquet_snappy_to_s3(s3_mock_client):
    """
    Verifies that PolarsParquetWriterToS3 can write and upload Parquet files with Snappy compression to S3.
    """
    df = pl.DataFrame({"x": [10, 20], "y": ["a", "b"]})
    writer = PolarsParquetWriterToS3(s3=s3_mock_client)

    writer.write(
        df, "compressed/snappy.parquet", bucket="bucket-x", compression="snappy"
    )

    s3_mock_client.upload_bytes.assert_called_once()
    args = s3_mock_client.upload_bytes.call_args[0]
    assert args[0] == "bucket-x"
    assert args[1] == "compressed/snappy.parquet"
    assert isinstance(args[2], bytes)
    assert len(args[2]) > 0
