import pytest
import json
from app.file_io.infrastructure.adapters.readers import JSONReaderFromS3


def test_json_reader_from_s3_reads_dict(s3_mock_client):
    """Reads a JSON object from S3 and verifies the returned dict."""
    data = {"framework": "FastAPI", "language": "Python"}
    s3_mock_client.download_string.return_value = json.dumps(data)

    reader = JSONReaderFromS3(s3=s3_mock_client)
    result = reader.read("info.json", bucket="test-bucket")

    assert isinstance(result, dict)
    assert result["framework"] == "FastAPI"


def test_json_reader_from_s3_reads_list(s3_mock_client):
    """Reads a JSON list from S3 and verifies the returned list."""
    data = [{"x": 1}, {"x": 2}]
    s3_mock_client.download_string.return_value = json.dumps(data)

    reader = JSONReaderFromS3(s3=s3_mock_client)
    result = reader.read("list.json", bucket="my-bucket")

    assert isinstance(result, list)
    assert result[0]["x"] == 1


def test_json_reader_from_s3_invalid_json(s3_mock_client):
    """Checks that malformed JSON from S3 raises JSONDecodeError."""
    s3_mock_client.download_string.return_value = "{ not valid json"

    reader = JSONReaderFromS3(s3=s3_mock_client)
    with pytest.raises(json.JSONDecodeError):
        reader.read("bad.json", bucket="bucket")
