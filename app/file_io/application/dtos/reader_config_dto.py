from pydantic import BaseModel

from app.file_io.domain.value_objects import StorageSource, FileFormat, WriterEngine


class ReaderConfigDTO(BaseModel):
    """
    DTO that encapsulates the configuration for a file writer.

    Attributes:
        source (StorageSource): The storage source (e.g., local or aws).
        file_format (FileFormat): The file format (e.g., csv, json, parquet, etc.).
        engine (WriterEngine): The specific writer engine to use.
    """

    source: StorageSource = StorageSource.LOCAL
    file_format: FileFormat = FileFormat.JSON
    engine: WriterEngine = WriterEngine.JSON
