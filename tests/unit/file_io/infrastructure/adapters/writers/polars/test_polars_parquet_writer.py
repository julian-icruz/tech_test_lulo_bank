import polars as pl
import pandas as pd

from app.file_io.infrastructure.adapters.writers import PolarsParquetWriter


def test_write_polars_parquet_creates_file_and_matches_content(tmp_path):
    """
    Writes a Polars DataFrame to a Parquet file and verifies the file content matches the original.
    """
    df = pl.DataFrame({"id": [1, 2], "value": ["A", "B"]})
    path = tmp_path / "output.parquet"

    writer = PolarsParquetWriter()
    writer.write(df, path)

    result = pd.read_parquet(path)
    expected = df.to_pandas()

    pd.testing.assert_frame_equal(result, expected)


def test_write_polars_parquet_with_snappy_compression(tmp_path):
    """
    Writes a Polars DataFrame to a local Parquet file using Snappy compression and verifies content.
    """
    df = pl.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    path = tmp_path / "compressed_snappy.parquet"

    from app.file_io.infrastructure.adapters.writers import PolarsParquetWriter

    writer = PolarsParquetWriter()
    writer.write(df, str(path), compression="snappy")

    result = pl.read_parquet(str(path))
    assert result.shape == (2, 2)
    assert result[1, "y"] == "b"
