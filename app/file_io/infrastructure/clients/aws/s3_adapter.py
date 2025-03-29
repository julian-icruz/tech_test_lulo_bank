import boto3
from botocore.exceptions import ClientError


class S3Adapter:
    """
    Adapter class that wraps boto3 to interact with AWS S3.

    Allows downloading and uploading files as strings or bytes,
    with the bucket passed explicitly per method call.
    """

    def __init__(self, region_name: str | None = None):
        """
        Initializes the boto3 S3 client.

        Args:
            region_name (str | None): Optional. Explicit region name.
                If not provided, will use:
                - AWS_DEFAULT_REGION from env
                - ~/.aws/config
                - boto3 fallback chain
        """
        self.client = boto3.client("s3", region_name=region_name)

    def download_string(self, bucket: str, key: str) -> str:
        """
        Download a UTF-8 string from S3.

        Args:
            bucket (str): The name of the S3 bucket.
            key (str): The S3 object key (file path).

        Returns:
            str: File content decoded as UTF-8.
        """
        try:
            response = self.client.get_object(Bucket=bucket, Key=key)
            return response["Body"].read().decode("utf-8")
        except ClientError as e:
            raise RuntimeError(
                f"Error downloading {key} from bucket {bucket}: {str(e)}"
            )

    def download_bytes(self, bucket: str, key: str) -> bytes:
        """
        Download raw bytes from S3.

        Args:
            bucket (str): The name of the S3 bucket.
            key (str): The S3 object key (file path).

        Returns:
            bytes: Raw binary content of the file.
        """
        try:
            response = self.client.get_object(Bucket=bucket, Key=key)
            return response["Body"].read()
        except ClientError as e:
            raise RuntimeError(
                f"Error downloading {key} from bucket {bucket}: {str(e)}"
            )

    def upload_string(self, bucket: str, key: str, content: str) -> None:
        """
        Upload a UTF-8 encoded string to S3.

        Args:
            bucket (str): The name of the S3 bucket.
            key (str): The S3 object key (file path).
            content (str): The string to upload.
        """
        try:
            self.client.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
        except ClientError as e:
            raise RuntimeError(f"Error uploading to {key} in bucket {bucket}: {str(e)}")

    def upload_bytes(self, bucket: str, key: str, content: bytes) -> None:
        """
        Upload raw bytes to S3.

        Args:
            bucket (str): The name of the S3 bucket.
            key (str): The S3 object key (file path).
            content (bytes): The binary content to upload.
        """
        try:
            self.client.put_object(Bucket=bucket, Key=key, Body=content)
        except ClientError as e:
            raise RuntimeError(f"Error uploading to {key} in bucket {bucket}: {str(e)}")
