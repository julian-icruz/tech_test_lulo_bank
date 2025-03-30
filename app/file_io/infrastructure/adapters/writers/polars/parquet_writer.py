import polars as pl
from app.file_io.domain.ports import FileWriter


class PolarsParquetWriter(FileWriter):
    """
    Writes a Polars DataFrame to a Parquet file locally.

    Args:
        data (pl.DataFrame): The DataFrame to write.
        path (str): The path to save the Parquet file.
        **kwargs: Additional parameters passed to pl.DataFrame.write_parquet().
    """

    def write(self, data: pl.DataFrame, path: str, **kwargs) -> None:
        data.write_parquet(path, **kwargs)
