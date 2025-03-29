import pandas as pd
from io import StringIO, BytesIO
from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class PandasCSVReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a CSV file from S3 and parses it into a pandas DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return pd.read_csv(StringIO(content), **kwargs)


@dataclass
class PandasJSONReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a JSON file from S3 and parses it into a pandas DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return pd.read_json(StringIO(content), **kwargs)


@dataclass
class PandasParquetReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a Parquet file from S3 and parses it into a pandas DataFrame.
    """

    def read(self, path: str, **kwargs) -> pd.DataFrame:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_bytes(bucket, path)
        return pd.read_parquet(BytesIO(content), **kwargs)
