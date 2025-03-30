import polars as pl
from io import BytesIO, StringIO
from dataclasses import dataclass

from app.file_io.domain.ports import FileWriter
from app.file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class PolarsCSVWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Polars DataFrame to a CSV file in AWS S3.
    """

    def write(self, data: pl.DataFrame, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        buffer = StringIO()
        data.write_csv(buffer, **kwargs)
        self.s3.upload_string(bucket, path, buffer.getvalue())


@dataclass
class PolarsParquetWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Polars DataFrame to a Parquet file in AWS S3.
    """

    def write(self, data: pl.DataFrame, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        buffer = BytesIO()
        data.write_parquet(buffer, **kwargs)
        buffer.seek(0)
        self.s3.upload_bytes(bucket, path, buffer.getvalue())
