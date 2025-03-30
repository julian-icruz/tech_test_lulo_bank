import pytest
import tempfile
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from unittest.mock import MagicMock


@pytest.fixture
def temp_csv_path():
    """Creates a temporary CSV file with given content and returns its file path."""

    def _create(content: str):
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
            f.write(content)
            return f.name

    return _create


@pytest.fixture
def temp_json_path():
    """Creates a temporary JSON file with given content and returns its file path."""

    def _create(content: str):
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
            f.write(content)
            return f.name

    return _create


@pytest.fixture
def temp_parquet_path():
    """Creates a temporary uncompressed Parquet file and returns its file path."""

    def _create(df: pd.DataFrame):
        table = pa.Table.from_pandas(df)
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            pq.write_table(table, f.name, compression=None)
            return f.name

    return _create


@pytest.fixture
def temp_parquet_path_snappy():
    """Creates a temporary Parquet file compressed with Snappy and returns its file path."""

    def _create(df: pd.DataFrame):
        table = pa.Table.from_pandas(df)
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            pq.write_table(table, f.name, compression="snappy")
            return f.name

    return _create


@pytest.fixture
def temp_yaml_path():
    """Creates a temporary YAML file with given content and returns its file path."""

    def _create(content: str):
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".yaml", delete=False) as f:
            f.write(content)
            return f.name

    return _create


@pytest.fixture
def s3_mock_client():
    """
    Provides a mock S3 client with download_string and download_bytes methods
    to simulate interaction with AWS S3.
    """
    client = MagicMock()
    return client
