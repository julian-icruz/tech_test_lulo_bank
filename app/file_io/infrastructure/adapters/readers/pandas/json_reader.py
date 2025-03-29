import pandas as pd
from app.file_io.domain.ports.file_reader import FileReader


class PandasJSONReader(FileReader):
    """
    Reads a JSON (newline-delimited) file from a local path using pandas.

    Args:
        path (str): The path to the JSON file.
        **kwargs: Extra parameters passed to pandas.read_json.

    Returns:
        pd.DataFrame: The contents of the JSON file as a DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        return pd.read_json(path, **kwargs)
