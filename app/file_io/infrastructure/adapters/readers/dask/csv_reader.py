import dask.dataframe as dd
from app.file_io.domain.ports.file_reader import FileReader


class DaskCSVReader(FileReader):
    """
    Reads a CSV file using Dask.

    Args:
        path (str): The path to the CSV file.
        **kwargs: Additional arguments passed to dask.dataframe.read_csv.

    Returns:
        dd.DataFrame: A Dask DataFrame for parallel processing.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        return dd.read_csv(path, **kwargs)
