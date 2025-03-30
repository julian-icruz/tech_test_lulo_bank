import yaml
from app.file_io.infrastructure.adapters.writers import YAMLWriterToS3


def test_yaml_writer_to_s3_writes_dict_correctly(s3_mock_client):
    """
    Writes a dictionary to S3 as YAML and verifies the uploaded content.
    """
    data = {"service": "backend", "enabled": True}
    writer = YAMLWriterToS3(s3=s3_mock_client)

    writer.write(data, "config.yaml", bucket="infra")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert args[0] == "infra"
    assert args[1] == "config.yaml"
    assert yaml.safe_load(args[2]) == data


def test_yaml_writer_to_s3_writes_list_correctly(s3_mock_client):
    """
    Writes a list to S3 as YAML and verifies the uploaded structure.
    """
    data = ["dev", "stage", "prod"]
    writer = YAMLWriterToS3(s3=s3_mock_client)

    writer.write(data, "envs.yaml", bucket="configs")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert yaml.safe_load(args[2]) == data


def test_yaml_writer_to_s3_with_encoding(s3_mock_client):
    """
    Writes YAML with unicode content to S3 and verifies encoding behavior.
    """
    data = {"emoji": "🐍"}
    writer = YAMLWriterToS3(s3=s3_mock_client)

    writer.write(data, "emoji.yaml", bucket="test-bucket", encoding="utf-8")

    s3_mock_client.upload_string.assert_called_once()
    _, _, content = s3_mock_client.upload_string.call_args[0]
    assert "🐍" in content
