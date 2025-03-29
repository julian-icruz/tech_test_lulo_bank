import pandas as pd
from io import BytesIO
from dataclasses import dataclass

from file_io.domain.ports import FileWriter
from file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class PandasCSVWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a pandas DataFrame to a CSV file in AWS S3.
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        csv_str = data.to_csv(**kwargs)
        self.s3.upload_string(bucket, path, csv_str)


@dataclass
class PandasJSONWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a pandas DataFrame to a JSON file in AWS S3.
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        json_str = data.to_json(**kwargs)
        self.s3.upload_string(bucket, path, json_str)


@dataclass
class PandasParquetWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a pandas DataFrame to a Parquet file in AWS S3.
    """

    def write(self, data: pd.DataFrame, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        buffer = BytesIO()
        data.to_parquet(buffer, **kwargs)
        buffer.seek(0)
        self.s3.upload_bytes(bucket, path, buffer.getvalue())
