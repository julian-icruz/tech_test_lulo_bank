import polars as pl

from app.file_io.infrastructure.adapters.readers import PolarsParquetReader


def test_polars_parquet_reader_basic(temp_parquet_path):
    """Reads a Parquet file with Polars and verifies its content."""
    import pandas as pd

    df_pd = pd.DataFrame({"a": [10, 20], "b": ["x", "y"]})
    path = temp_parquet_path(df_pd)

    reader = PolarsParquetReader()
    df = reader.read(path)
    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[0, "a"] == 10


def test_polars_parquet_reader_snappy(temp_parquet_path_snappy):
    """Reads a snappy-compressed Parquet file using Polars."""
    import pandas as pd

    df_pd = pd.DataFrame({"m": [1, 2], "n": ["u", "v"]})
    path = temp_parquet_path_snappy(df_pd)

    reader = PolarsParquetReader()
    df = reader.read(path)
    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[1, "n"] == "v"
