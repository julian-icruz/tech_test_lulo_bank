import polars as pl
from file_io.domain.ports.file_reader import FileReader


class PolarsParquetReader(FileReader):
    """
    Reads a Parquet file using polars.

    Args:
        path (str): The path to the Parquet file.
        **kwargs: Additional arguments passed to polars.read_parquet.

    Returns:
        pl.DataFrame: The Parquet data as a Polars DataFrame.
    """

    def read(self, path: str, **kwargs) -> pl.DataFrame:
        return pl.read_parquet(path, **kwargs)
