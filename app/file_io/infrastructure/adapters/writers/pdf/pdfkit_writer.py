import pdfkit
from file_io.domain.ports import FileWriter


class PDFKitWriter(FileWriter):
    """
    Writes HTML content to a PDF file locally using pdfkit.

    Args:
        data (str): HTML content to render as PDF.
        path (str): Output path for the PDF.
        **kwargs: Additional pdfkit options (e.g., configuration, options).
    """

    def write(self, data: str, path: str, **kwargs) -> None:
        pdfkit.from_string(data, path, **kwargs)
