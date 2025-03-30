import pytest

from app.file_io.infrastructure.adapters.writers import PDFWriterToS3


def test_pdf_writer_to_s3_uploads_binary(s3_mock_client):
    """
    Uploads binary PDF content to S3 and verifies that bytes are correctly passed.
    """
    content = b"%PDF-1.4 binary content"
    writer = PDFWriterToS3(s3=s3_mock_client)

    writer.write(content, "files/report.pdf", bucket="pdf-bucket")

    s3_mock_client.upload_bytes.assert_called_once()
    bucket, key, uploaded_content = s3_mock_client.upload_bytes.call_args[0]

    assert bucket == "pdf-bucket"
    assert key == "files/report.pdf"
    assert isinstance(uploaded_content, bytes)
    assert uploaded_content.startswith(b"%PDF")


def test_pdf_writer_to_s3_uploads_pdf_bytes(s3_mock_client, sample_html):
    """
    Writes PDF content as bytes to S3 using the PDFWriterToS3 and verifies upload.
    """
    writer = PDFWriterToS3(s3=s3_mock_client)
    pdf_data = sample_html.encode("utf-8")

    writer.write(pdf_data, "test_report.pdf", bucket="test-bucket")

    s3_mock_client.upload_bytes.assert_called_once()
    called_bucket, key, uploaded_content = s3_mock_client.upload_bytes.call_args[0]
    assert called_bucket == "test-bucket"
    assert key == "test_report.pdf"
    assert isinstance(uploaded_content, bytes)


def test_pdf_writer_to_s3_missing_bucket_raises(sample_html):
    """
    Validates that omitting 'bucket' in kwargs raises a ValueError.
    """
    writer = PDFWriterToS3(s3=object())

    with pytest.raises(ValueError, match="Missing required 'bucket'"):
        writer.write(b"%PDF-1.4 content", "no_bucket.pdf")


def test_pdf_writer_to_s3_rejects_non_bytes(s3_mock_client):
    """
    Ensures PDFWriterToS3 only accepts bytes-like content.
    """
    writer = PDFWriterToS3(s3=s3_mock_client)
    with pytest.raises(TypeError):
        writer.write("<html>Not Bytes</html>", "should_fail.pdf", bucket="test-bucket")
