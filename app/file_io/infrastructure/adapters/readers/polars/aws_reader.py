import polars as pl
from io import BytesIO, StringIO
from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class PolarsCSVReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a CSV file from S3 and parses it into a Polars DataFrame.
    """

    def read(self, path: str, **kwargs) -> pl.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return pl.read_csv(StringIO(content), **kwargs)


@dataclass
class PolarsParquetReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a Parquet file from S3 and parses it into a Polars DataFrame.
    """

    def read(self, path: str, **kwargs) -> pl.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_bytes(bucket, path)
        return pl.read_parquet(BytesIO(content), **kwargs)
