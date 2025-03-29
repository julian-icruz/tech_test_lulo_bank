import dask.dataframe as dd
from file_io.domain.ports.file_reader import FileReader


class DaskParquetReader(FileReader):
    """
    Reads a Parquet file using Dask.

    Args:
        path (str): The path to the Parquet file.
        **kwargs: Additional arguments passed to dask.dataframe.read_parquet.

    Returns:
        dd.DataFrame: A Dask DataFrame for parallel processing.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        return dd.read_parquet(path, **kwargs)
