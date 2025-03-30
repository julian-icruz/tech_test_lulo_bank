from dataclasses import dataclass
from app.file_io.domain.ports import FileWriter
from app.file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class PDFWriterToS3(BaseS3Writer, FileWriter):
    """
    Uploads raw PDF bytes to a file in AWS S3.

    Args:
        data (bytes): Binary PDF content.
        path (str): S3 object key (file path).
        **kwargs: Must include 'bucket'.
    """

    def write(self, data: bytes, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        self.s3.upload_bytes(bucket, path, data)
