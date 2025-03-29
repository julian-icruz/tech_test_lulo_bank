import polars as pl
from app.file_io.domain.ports import FileReader


class PolarsCSVReader(FileReader):
    """
    Reads a CSV file using polars.

    Args:
        path (str): The path to the CSV file.
        **kwargs: Additional arguments passed to polars.read_csv.

    Returns:
        pl.DataFrame: The CSV data as a Polars DataFrame.
    """

    def read(self, path: str, **kwargs) -> pl.DataFrame:
        return pl.read_csv(path, **kwargs)
