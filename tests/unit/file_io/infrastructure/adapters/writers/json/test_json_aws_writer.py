import json
from app.file_io.infrastructure.adapters.writers import JSONWriterToS3


def test_json_writer_to_s3_writes_dict_correctly(s3_mock_client):
    """
    Writes a dictionary as JSON to a mocked S3 bucket and verifies the content.
    """
    data = {"project": "Lulo", "language": "Python"}
    writer = JSONWriterToS3(s3=s3_mock_client)

    writer.write(data, "data.json", bucket="test-bucket")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert args[0] == "test-bucket"
    assert args[1] == "data.json"
    assert json.loads(args[2]) == data


def test_json_writer_to_s3_writes_list_correctly(s3_mock_client):
    """
    Writes a list of objects as JSON to S3 and verifies content and key.
    """
    data = [{"id": 1}, {"id": 2}]
    writer = JSONWriterToS3(s3=s3_mock_client)

    writer.write(data, "list.json", bucket="my-bucket")

    s3_mock_client.upload_string.assert_called_once()
    args = s3_mock_client.upload_string.call_args[0]
    assert args[0] == "my-bucket"
    assert args[1] == "list.json"
    assert json.loads(args[2]) == data


def test_json_writer_to_s3_with_indent(s3_mock_client):
    """
    Writes a JSON with indentation and checks if the formatting is passed to upload.
    """
    data = {"x": 1, "y": 2}
    writer = JSONWriterToS3(s3=s3_mock_client)

    writer.write(data, "pretty.json", bucket="bucket-name", indent=2)

    s3_mock_client.upload_string.assert_called_once()
    _, _, content = s3_mock_client.upload_string.call_args[0]
    assert content.startswith("{\n")
    assert '"x": 1' in content
