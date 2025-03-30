import pandas as pd

from app.file_io.infrastructure.adapters.writers import PandasParquetWriter


def test_write_parquet_creates_file_and_reads_correctly(sample_dataframe, tmp_path):
    """
    Writes a DataFrame to a Parquet file and verifies it reads back correctly.
    """
    path = tmp_path / "test.parquet"
    writer = PandasParquetWriter()
    writer.write(sample_dataframe, path)

    result = pd.read_parquet(path)
    pd.testing.assert_frame_equal(result, sample_dataframe)


def test_write_parquet_with_snappy_compression(sample_dataframe, tmp_path):
    """
    Writes a Parquet file using Snappy compression and verifies structure.
    """
    path = tmp_path / "compressed.parquet"
    writer = PandasParquetWriter()
    writer.write(sample_dataframe, path, compression="snappy")

    result = pd.read_parquet(path)
    pd.testing.assert_frame_equal(result, sample_dataframe)
