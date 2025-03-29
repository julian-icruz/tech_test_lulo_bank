from abc import ABC
from dataclasses import dataclass

from file_io.infrastructure.clients import S3Adapter


@dataclass
class BaseS3Writer(ABC):
    """
    Abstract base class for all S3 file writers.

    Provides a shared S3 adapter instance and helper method to extract
    the S3 bucket name from kwargs. This prevents repeated logic across
    all concrete writer implementations targeting AWS S3.

    Attributes:
        s3 (S3Adapter): Shared S3 adapter to perform upload operations.
    """

    s3: S3Adapter

    def _get_bucket(self, kwargs: dict) -> str:
        """
        Extracts the 'bucket' key from kwargs.
        Raises an error if the bucket is not provided.

        Args:
            kwargs (dict): Keyword arguments passed to the write method.

        Returns:
            str: The extracted bucket name.

        Raises:
            ValueError: If 'bucket' is not found in kwargs.
        """
        bucket = kwargs.pop("bucket", None)
        if not bucket:
            raise ValueError("Missing required 'bucket' in kwargs.")
        return bucket
