from dataclasses import dataclass
from file_io.domain.ports import FileWriter
from file_io.infrastructure.adapters.writers.base.s3_writer import BaseS3Writer


@dataclass
class HTMLWriterToS3(BaseS3Writer, FileWriter):
    """
    Uploads raw HTML content as a file to AWS S3.

    Args:
        data (str): A raw HTML string.
        path (str): The S3 object key.
        **kwargs: Must include 'bucket' in kwargs.
    """

    def write(self, data: str, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        self.s3.upload_string(bucket, path, data)
