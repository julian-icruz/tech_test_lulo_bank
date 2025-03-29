from weasyprint import HTML
from file_io.domain.ports import FileWriter


class WeasyPrintWriter(FileWriter):
    """
    Writes HTML content to a PDF file locally using WeasyPrint.

    Args:
        data (str): HTML content to render as PDF.
        path (str): Output path for the PDF.
        **kwargs: Additional weasyprint options.
    """

    def write(self, data: str, path: str, **kwargs) -> None:
        HTML(string=data).write_pdf(target=path, **kwargs)
