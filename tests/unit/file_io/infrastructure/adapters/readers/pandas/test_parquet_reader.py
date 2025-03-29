import pytest
import pandas as pd

from app.file_io.infrastructure.adapters.readers import PandasParquetReader


def test_read_parquet_file(temp_parquet_path):
    """Reads a basic uncompressed Parquet file and checks if the DataFrame is correctly loaded."""
    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    path = temp_parquet_path(df)
    reader = PandasParquetReader()
    result = reader.read(path)
    pd.testing.assert_frame_equal(result, df)


def test_read_parquet_file_with_snappy_compression(temp_parquet_path_snappy):
    """Reads a Parquet file compressed with Snappy and verifies the DataFrame content."""
    df = pd.DataFrame({"x": [10, 20], "y": ["foo", "bar"]})
    path = temp_parquet_path_snappy(df)
    reader = PandasParquetReader()
    result = reader.read(path)
    pd.testing.assert_frame_equal(result, df)


def test_read_parquet_file_missing(temp_parquet_path):
    """Checks that reading a non-existent Parquet file raises a FileNotFoundError."""
    reader = PandasParquetReader()
    with pytest.raises(FileNotFoundError):
        reader.read("non_existent_file.parquet")
