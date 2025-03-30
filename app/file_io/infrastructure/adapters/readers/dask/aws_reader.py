import dask.dataframe as dd

from dataclasses import dataclass

from app.file_io.domain.ports import FileReader
from app.file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class DaskCSVReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a CSV file from AWS S3 and loads it into a Dask DataFrame.

    Dask requires file paths for reading, so the CSV content is first downloaded
    from S3 as a string and then written to a temporary file, which is read by Dask.

    Args:
        path (str): The S3 object key of the CSV file.
        bucket (str): Required keyword argument specifying the name of the S3 bucket.
        **kwargs: Additional parameters passed to dask.dataframe.read_csv.

    Returns:
        dd.DataFrame: A Dask DataFrame containing the contents of the CSV file.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return self._read_with_tempfile(
            content, ".csv", binary=False, reader_fn=dd.read_csv, **kwargs
        )


@dataclass
class DaskParquetReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a Parquet file from AWS S3 and loads it into a Dask DataFrame.

    Dask requires file paths for reading, so the Parquet content is first downloaded
    from S3 as raw bytes and written to a temporary file, which is then read by Dask.

    Args:
        path (str): The S3 object key of the Parquet file.
        bucket (str): Required keyword argument specifying the name of the S3 bucket.
        **kwargs: Additional parameters passed to dask.dataframe.read_parquet.

    Returns:
        dd.DataFrame: A Dask DataFrame containing the contents of the Parquet file.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_bytes(bucket, path)
        return self._read_with_tempfile(
            content, ".parquet", binary=True, reader_fn=dd.read_parquet, **kwargs
        )
