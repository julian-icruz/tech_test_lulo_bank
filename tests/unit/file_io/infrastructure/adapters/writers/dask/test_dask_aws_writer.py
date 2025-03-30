import pytest
import pandas as pd
import dask.dataframe as dd

from app.file_io.infrastructure.adapters.writers import DaskParquetWriterToS3


def test_dask_parquet_writer_to_s3(s3_mock_client, tmp_path):
    """
    Verifies that DaskParquetWriterToS3 writes a Parquet file to S3.
    """
    data = dd.from_pandas(
        pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]}), npartitions=1
    )
    writer = DaskParquetWriterToS3(s3=s3_mock_client)
    path = tmp_path / "test_parquet_file.parquet"
    s3_mock_client.upload_bytes.return_value = None
    writer.write(data, path, bucket="my-bucket")
    s3_mock_client.upload_bytes.assert_called_once()


def test_dask_parquet_writer_to_s3_empty_dataframe(s3_mock_client, tmp_path):
    """
    Verifies that DaskParquetWriterToS3 raises an error for empty DataFrame writes.
    """
    empty_df = dd.from_pandas(pd.DataFrame(columns=["col1", "col2"]), npartitions=1)
    writer = DaskParquetWriterToS3(s3=s3_mock_client)
    path = tmp_path / "empty_parquet_file.parquet"

    with pytest.raises(ValueError):
        writer.write(empty_df, path, bucket="my-bucket")
