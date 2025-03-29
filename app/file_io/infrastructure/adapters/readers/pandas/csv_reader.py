import pandas as pd
from file_io.domain.ports import FileReader


class PandasCSVReader(FileReader):
    """
    Reads a CSV file from a local path using pandas.

    Args:
        path (str): The path to the CSV file.
        **kwargs: Extra parameters passed to pandas.read_csv.

    Returns:
        pd.DataFrame: The contents of the CSV file as a DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        return pd.read_csv(path, **kwargs)
