import yaml
from dataclasses import dataclass
from typing import Any

from file_io.domain.ports import FileWriter
from file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class YAMLWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Python object to a YAML file in AWS S3
    using PyYAML.
    """

    def write(self, data: Any, path: str, **kwargs) -> None:
        bucket = self._get_bucket(kwargs)
        content = yaml.safe_dump(data, **kwargs)
        self.s3.upload_string(bucket, path, content)
