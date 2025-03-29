from file_io.domain.ports import FileWriter


class HTMLWriter(FileWriter):
    """
    Writes raw HTML content to a local file.

    Args:
        data (str): A raw HTML string.
        path (str): The file path to write to.
        **kwargs: Optional encoding and file options.
    """

    def write(self, data: str, path: str, **kwargs) -> None:
        encoding = kwargs.pop("encoding", "utf-8")
        with open(path, "w", encoding=encoding) as f:
            f.write(data)
