import yaml
from dataclasses import dataclass
from typing import Any

from app.file_io.domain.ports import FileWriter
from app.file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class YAMLWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Python object to a YAML file in AWS S3 using PyYAML.

    Args:
        data (Any): The Python object to serialize (e.g., dict, list).
        path (str): The destination path in S3.
        **kwargs:
            - bucket (str): Required. S3 bucket name.
            - encoding (str, optional): Extracted but unused (YAML returns string).
            - Any other args for yaml.safe_dump().
    """

    def write(self, data: Any, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        kwargs.pop("encoding", None)  # safely discard encoding if passed
        content = yaml.safe_dump(data, allow_unicode=True, **kwargs)
        self.s3.upload_string(bucket, path, content)
