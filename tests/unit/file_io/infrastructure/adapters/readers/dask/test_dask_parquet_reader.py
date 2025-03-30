import pytest
import pandas as pd

from app.file_io.infrastructure.adapters.readers import DaskParquetReader


def test_dask_parquet_reader_basic(temp_parquet_path):
    """Reads a basic Parquet file with Dask and validates content."""
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    path = temp_parquet_path(df)
    reader = DaskParquetReader()
    result = reader.read(path).compute()

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 2)
    assert result.iloc[1]["b"] == "y"


def test_dask_parquet_reader_snappy_compression(temp_parquet_path_snappy):
    """Reads a Snappy-compressed Parquet file using Dask."""
    df = pd.DataFrame({"z": [10, 20], "label": ["ok", "fail"]})
    path = temp_parquet_path_snappy(df)
    reader = DaskParquetReader()
    result = reader.read(path).compute()

    assert result.iloc[0]["z"] == 10
    assert result.iloc[1]["label"] == "fail"


def test_dask_parquet_reader_missing():
    """Raises FileNotFoundError when Parquet file is missing."""
    reader = DaskParquetReader()
    with pytest.raises(FileNotFoundError):
        reader.read("missing_file.parquet").compute()
