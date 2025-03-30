import dask.dataframe as dd
from app.file_io.domain.ports import FileWriter


class DaskParquetWriter(FileWriter):
    """
    Writes a Dask DataFrame to a local Parquet file.

    Args:
        data (dd.DataFrame): The Dask DataFrame to write.
        path (str): The output file path or directory.
        **kwargs: Additional arguments passed to `dask.dataframe.to_parquet`.

    Notes:
        - This writes to a directory, not a single .parquet file.
        - By default, writes without index unless overridden via kwargs.
    """

    def write(self, data: dd.DataFrame, path: str, **kwargs) -> None:
        data.to_parquet(path, **kwargs)
