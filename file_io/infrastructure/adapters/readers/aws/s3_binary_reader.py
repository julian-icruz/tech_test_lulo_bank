from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.clients import S3Adapter


@dataclass
class S3BinaryReader(FileReader):
    """
    Reader for binary files (Parquet, Snappy, PDF, etc.) from S3.
    Returns the file as raw bytes.
    """

    s3: S3Adapter

    def read(self, path: str, **kwargs) -> bytes:
        bucket = kwargs.pop("bucket")
        return self.s3.download_bytes(bucket=bucket, key=path)
