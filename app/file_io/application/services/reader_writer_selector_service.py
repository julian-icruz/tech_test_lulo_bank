from dataclasses import dataclass

from app.file_io.domain.ports import FileReader, FileWriter
from app.file_io.application.dtos import WriterConfigDTO, ReaderConfigDTO


@dataclass
class ReaderWriterSelectorService:
    readers: dict[str, dict[str, FileReader]]
    writers: dict[str, dict[str, FileWriter]]

    def __call__(
        self, operation_type: str, config: WriterConfigDTO | ReaderConfigDTO
    ) -> FileReader | FileWriter:
        """
        Selects the appropriate reader or writer based on the given configuration.

        Args:
            operation_type (str): Type of operation ('reader' or 'writer').
            config (WriterConfigDTO | ReaderConfigDTO): Configuration object with source, file_format, and engine.

        Returns:
            Any: The corresponding file reader or writer instance.
        """
        source = config.source.value
        file_format = config.file_format.value
        engine = config.engine.value

        reader_writer = {
            "reader": self.readers,
            "writer": self.writers,
        }
        return reader_writer[operation_type][source][file_format][engine]
