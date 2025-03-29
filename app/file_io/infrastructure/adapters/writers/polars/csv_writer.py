import polars as pl
from file_io.domain.ports import FileWriter


class PolarsCSVWriter(FileWriter):
    """
    Writes a Polars DataFrame to a CSV file locally.

    Args:
        data (pl.DataFrame): The DataFrame to write.
        path (str): The path to save the CSV file.
        **kwargs: Additional parameters passed to pl.DataFrame.write_csv().
    """

    def write(self, data: pl.DataFrame, path: str, **kwargs) -> None:
        data.write_csv(path, **kwargs)
