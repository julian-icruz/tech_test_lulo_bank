import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from io import BytesIO


from app.file_io.infrastructure.adapters.readers import (
    PandasCSVReaderFromS3,
    PandasJSONReaderFromS3,
    PandasParquetReaderFromS3,
)


def test_csv_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a CSV file from S3 using a mocked S3 client and returns a valid DataFrame."""
    csv_data = "col1,col2\n1,2\n3,4"
    s3_mock_client.download_string.return_value = csv_data

    reader = PandasCSVReaderFromS3(s3=s3_mock_client)
    df = reader.read("path/to/file.csv", bucket="my-bucket")

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.iloc[0]["col1"] == 1


def test_json_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a JSON file from S3 using a mocked S3 client and returns a valid DataFrame."""
    json_data = '[{"a": 10, "b": 20}, {"a": 30, "b": 40}]'
    s3_mock_client.download_string.return_value = json_data

    reader = PandasJSONReaderFromS3(s3=s3_mock_client)
    df = reader.read("some/file.json", bucket="data-bucket")

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df["b"].tolist() == [20, 40]


def test_parquet_reader_from_s3_reads_correctly(s3_mock_client):
    """Reads a Parquet file from S3 using a mocked S3 client and returns a valid DataFrame."""
    df_expected = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    table = pa.Table.from_pandas(df_expected)
    buffer = BytesIO()
    pq.write_table(table, buffer)
    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = PandasParquetReaderFromS3(s3=s3_mock_client)
    df_result = reader.read("data/file.parquet", bucket="my-bucket")

    pd.testing.assert_frame_equal(df_result, df_expected)


def test_parquet_reader_from_s3_reads_snappy_correctly(s3_mock_client):
    """Reads a Snappy-compressed Parquet file from S3 using a mocked S3 client and returns a valid DataFrame."""
    df_expected = pd.DataFrame({"x": [100, 200], "y": ["foo", "bar"]})
    table = pa.Table.from_pandas(df_expected)
    buffer = BytesIO()
    pq.write_table(table, buffer, compression="snappy")
    s3_mock_client.download_bytes.return_value = buffer.getvalue()

    reader = PandasParquetReaderFromS3(s3=s3_mock_client)
    df_result = reader.read("data/snappy_file.parquet", bucket="my-bucket")

    pd.testing.assert_frame_equal(df_result, df_expected)
