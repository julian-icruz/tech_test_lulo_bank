import pandas as pd

from app.file_io.domain.ports import FileWriter


class PandasJSONWriter(FileWriter):
    """
    Writes a pandas DataFrame to a JSON file locally.

    Args:
        data (pd.DataFrame): The DataFrame to write.
        path (str): The path to save the JSON file.
        **kwargs: Additional parameters passed to pandas.to_json().
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        data.to_json(path, **kwargs)
