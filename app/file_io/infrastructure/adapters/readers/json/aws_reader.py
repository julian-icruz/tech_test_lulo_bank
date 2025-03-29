import json
from dataclasses import dataclass

from file_io.domain.ports import FileReader
from file_io.infrastructure.adapters.readers import BaseS3Reader


@dataclass
class JSONReaderFromS3(BaseS3Reader, FileReader):
    """
    Downloads a JSON file from S3 and parses it using Python's built-in json module.

    Returns:
        dict | list: Parsed JSON object.
    """

    def read(self, path: str, **kwargs) -> dict:
        bucket = self._get_bucket(kwargs)
        content = self.s3.download_string(bucket, path)
        return json.loads(content)
