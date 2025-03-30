import pytest
import yaml
from app.file_io.infrastructure.adapters.readers import YAMLReaderFromS3


def test_yaml_reader_from_s3_reads_dict(s3_mock_client):
    """Reads a YAML dict from S3 and verifies the returned object."""
    data = {"service": "Lulo", "enabled": True}
    s3_mock_client.download_string.return_value = yaml.dump(data)

    reader = YAMLReaderFromS3(s3=s3_mock_client)
    result = reader.read("config.yaml", bucket="bucket-yaml")

    assert isinstance(result, dict)
    assert result["service"] == "Lulo"
    assert result["enabled"] is True


def test_yaml_reader_from_s3_reads_list(s3_mock_client):
    """Reads a YAML list from S3 and verifies the returned structure."""
    data = ["dev", "staging", "prod"]
    s3_mock_client.download_string.return_value = yaml.dump(data)

    reader = YAMLReaderFromS3(s3=s3_mock_client)
    result = reader.read("envs.yaml", bucket="infra")

    assert isinstance(result, list)
    assert result[-1] == "prod"


def test_yaml_reader_from_s3_invalid_content(s3_mock_client):
    """Checks that malformed YAML from S3 raises YAMLError."""
    s3_mock_client.download_string.return_value = "{ broken: yaml"

    reader = YAMLReaderFromS3(s3=s3_mock_client)
    with pytest.raises(yaml.YAMLError):
        reader.read("broken.yaml", bucket="some-bucket")
