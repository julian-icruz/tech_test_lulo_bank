from abc import ABC
from dataclasses import dataclass

from file_io.infrastructure.clients import S3Adapter


@dataclass
class BaseS3Reader(ABC):
    """
    Abstract base class for all S3 readers.

    Provides a shared S3 adapter and helper method to extract
    the S3 bucket name from kwargs.

    This avoids repeating logic in each concrete AWS reader.
    """

    s3: S3Adapter

    def _get_bucket(self, kwargs: dict) -> str:
        """
        Extracts the 'bucket' key from kwargs.
        Raises an error if it's missing.

        Args:
            kwargs (dict): Keyword arguments passed to the read method.

        Returns:
            str: The extracted bucket name.
        """
        bucket = kwargs.pop("bucket", None)
        if not bucket:
            raise ValueError("Missing required 'bucket' in kwargs.")
        return bucket
