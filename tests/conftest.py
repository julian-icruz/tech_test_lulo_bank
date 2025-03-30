import pytest
import tempfile
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from unittest.mock import MagicMock


# ------------------------------- READERS --------------------------------
def _create_temp_file(content: str, suffix: str, binary: bool = False):
    """Helper function to create a temporary file with given content and suffix."""
    mode = "wb+" if binary else "w+"
    with tempfile.NamedTemporaryFile(mode=mode, suffix=suffix, delete=False) as f:
        if binary:
            f.write(content)
        else:
            f.write(content)
        return f.name


@pytest.fixture
def temp_csv_path():
    def _create(content: str):
        return _create_temp_file(content, ".csv")

    return _create


@pytest.fixture
def temp_json_path():
    def _create(content: str):
        return _create_temp_file(content, ".json")

    return _create


@pytest.fixture
def temp_yaml_path():
    def _create(content: str):
        return _create_temp_file(content, ".yaml")

    return _create


@pytest.fixture
def temp_parquet_path():
    def _create(df: pd.DataFrame):
        table = pa.Table.from_pandas(df)
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            pq.write_table(table, f.name, compression=None)
            return f.name

    return _create


@pytest.fixture
def temp_parquet_path_snappy():
    def _create(df: pd.DataFrame):
        table = pa.Table.from_pandas(df)
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            pq.write_table(table, f.name, compression="snappy")
            return f.name

    return _create


@pytest.fixture
def s3_mock_client():
    """
    Provides a mock S3 client with download_string and download_bytes methods
    to simulate interaction with AWS S3.
    """
    return MagicMock()


# ------------------------------- WRITERS --------------------------------
@pytest.fixture
def sample_dataframe():
    """Returns a simple sample DataFrame for CSV writing tests."""
    return pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
