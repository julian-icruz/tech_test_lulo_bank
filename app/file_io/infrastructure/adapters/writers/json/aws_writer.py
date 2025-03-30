import json
from dataclasses import dataclass
from typing import Any

from app.file_io.domain.ports import FileWriter
from app.file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class JSONWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Python object to a JSON file in AWS S3
    using Python's built-in json module.
    """

    def write(self, data: Any, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        content = json.dumps(data, **kwargs)
        self.s3.upload_string(bucket, path, content)
