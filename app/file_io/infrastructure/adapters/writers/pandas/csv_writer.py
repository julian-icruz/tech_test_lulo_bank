import pandas as pd

from file_io.domain.ports import FileWriter


class PandasCSVWriter(FileWriter):
    """
    Writes a pandas DataFrame to a CSV file locally.

    Args:
        data (pd.DataFrame): The DataFrame to write.
        path (str): The path to save the CSV file.
        **kwargs: Additional parameters passed to pandas.to_csv().
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        data.to_csv(path, **kwargs)
