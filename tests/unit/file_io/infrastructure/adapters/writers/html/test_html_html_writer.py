from app.file_io.infrastructure.adapters.writers import HTMLWriterToS3


def test_html_writer_to_s3_uploads_correctly(s3_mock_client):
    """
    Writes HTML content to S3 and verifies the upload string content.
    """
    content = "<html><body><h2>S3 Upload Test</h2></body></html>"
    writer = HTMLWriterToS3(s3=s3_mock_client)

    writer.write(content, "reports/test.html", bucket="my-html-bucket")

    s3_mock_client.upload_string.assert_called_once()
    bucket, key, uploaded_content = s3_mock_client.upload_string.call_args[0]

    assert bucket == "my-html-bucket"
    assert key == "reports/test.html"
    assert content in uploaded_content


def test_html_writer_to_s3_with_unicode(s3_mock_client):
    """
    Uploads an HTML string with emojis to S3 and verifies the encoding is preserved.
    """
    content = "<p>¡Hola 🐍 desde S3!</p>"
    writer = HTMLWriterToS3(s3=s3_mock_client)

    writer.write(content, "emoji.html", bucket="unicode-bucket")

    s3_mock_client.upload_string.assert_called_once()
    _, _, uploaded_content = s3_mock_client.upload_string.call_args[0]

    assert "🐍" in uploaded_content
