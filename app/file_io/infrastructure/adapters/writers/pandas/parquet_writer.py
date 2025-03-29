import pandas as pd
from file_io.domain.ports import FileWriter


class PandasParquetWriter(FileWriter):
    """
    Writes a pandas DataFrame to a Parquet file locally.

    Args:
        data (pd.DataFrame): The DataFrame to write.
        path (str): The path to save the Parquet file.
        **kwargs: Additional parameters passed to pandas.to_parquet().
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        data.to_parquet(path, **kwargs)
