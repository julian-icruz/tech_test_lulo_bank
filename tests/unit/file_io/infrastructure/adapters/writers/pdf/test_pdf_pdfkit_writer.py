import pytest
from app.file_io.infrastructure.adapters.writers import PDFKitWriter


def test_pdfkit_writer_creates_pdf(tmp_path, sample_html):
    """
    Writes a PDF file from HTML using PDFKit and checks if the file exists and is not empty.
    """
    output_path = tmp_path / "output.pdf"
    writer = PDFKitWriter()

    writer.write(sample_html, str(output_path))

    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_pdfkit_writer_empty_html_creates_non_empty_file(tmp_path):
    """
    Writes an empty HTML string and ensures the PDF file is still created and not empty.
    """
    path = tmp_path / "empty.pdf"
    writer = PDFKitWriter()
    writer.write("", str(path))

    assert path.exists()
    assert path.stat().st_size > 0


def test_pdfkit_writer_invalid_path_raises_error(sample_html):
    """
    Attempts to write to an invalid file path and expects an OSError or IOError.
    """
    writer = PDFKitWriter()
    invalid_path = "/invalid/path/output.pdf"

    with pytest.raises((OSError, IOError, Exception)):
        writer.write(sample_html, invalid_path)


def test_pdfkit_writer_with_custom_options(tmp_path, sample_html):
    """
    Writes PDF using pdfkit with custom options and ensures file is created.
    """
    path = tmp_path / "landscape.pdf"
    writer = PDFKitWriter()
    options = {"orientation": "Landscape"}

    writer.write(sample_html, str(path), options=options)

    assert path.exists()
    assert path.stat().st_size > 0
