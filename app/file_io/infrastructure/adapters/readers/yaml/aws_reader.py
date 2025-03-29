import yaml
from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class YAMLReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a YAML file from S3 and parses it using PyYAML.

    Returns:
        dict | list: Parsed YAML structure.
    """

    def read(self, path: str, **kwargs) -> dict:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return yaml.safe_load(content)
