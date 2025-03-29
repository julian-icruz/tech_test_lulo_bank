import pandas as pd
from file_io.domain.ports.file_reader import FileReader


class PandasParquetReader(FileReader):
    """
    Reads a Parquet file from a local path using pandas.

    Args:
        path (str): The path to the Parquet file.
        **kwargs: Extra parameters passed to pandas.read_parquet.

    Returns:
        pd.DataFrame: The contents of the Parquet file as a DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        return pd.read_parquet(path, **kwargs)
