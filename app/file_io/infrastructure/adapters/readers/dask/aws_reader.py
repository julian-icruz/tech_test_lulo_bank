import dask.dataframe as dd
from io import StringIO, BytesIO
from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class DaskCSVReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a CSV file from S3 and parses it into a Dask DataFrame.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return dd.read_csv(StringIO(content), **kwargs)


@dataclass
class DaskParquetReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a Parquet file from S3 and parses it into a Dask DataFrame.
    """

    def read(self, path: str, **kwargs) -> dd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_bytes(bucket, path)
        return dd.read_parquet(BytesIO(content), **kwargs)
