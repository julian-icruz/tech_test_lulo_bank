import json
import pandas as pd

from io import BytesIO

from app.file_io.infrastructure.adapters.writers import (
    PandasCSVWriterToS3,
    PandasJSONWriterToS3,
    PandasParquetWriterToS3,
)


def test_csv_writer_to_s3_uploads_correct_string(sample_dataframe, s3_mock_client):
    """
    Writes a DataFrame to CSV and ensures correct string upload to S3.
    """
    writer = PandasCSVWriterToS3(s3=s3_mock_client)
    writer.write(sample_dataframe, "test.csv", bucket="my-bucket")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert args[0] == "my-bucket"
    assert args[1] == "test.csv"
    assert "col1" in args[2]


def test_json_writer_to_s3_uploads_json_string(sample_dataframe, s3_mock_client):
    """
    Writes a DataFrame to JSON and verifies string upload to S3.
    """
    writer = PandasJSONWriterToS3(s3=s3_mock_client)
    writer.write(sample_dataframe, "file.json", bucket="data-bucket")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    json.loads(args[2])


def test_parquet_writer_to_s3_uploads_bytes(sample_dataframe, s3_mock_client):
    """
    Writes a DataFrame to Parquet and verifies bytes upload to S3.
    """
    writer = PandasParquetWriterToS3(s3=s3_mock_client)
    writer.write(sample_dataframe, "data.parquet", bucket="my-bucket")

    s3_mock_client.upload_bytes.assert_called_once()
    args = s3_mock_client.upload_bytes.call_args[0]
    buffer = BytesIO(args[2])
    df = pd.read_parquet(buffer)
    pd.testing.assert_frame_equal(df, sample_dataframe)
