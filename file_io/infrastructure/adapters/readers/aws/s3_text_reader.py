from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.clients import S3Adapter


@dataclass
class S3TextReader(FileReader):
    """
    Reader for any text-based file (CSV, JSON, YAML, etc.) from S3.
    Returns the file as a decoded UTF-8 string.
    """

    s3: S3Adapter

    def read(self, path: str, **kwargs) -> str:
        bucket = kwargs.pop("bucket")
        return self.s3.download_string(bucket=bucket, key=path)
