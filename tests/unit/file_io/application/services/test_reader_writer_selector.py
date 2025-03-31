import pytest
from app.file_io.domain.ports import FileReader, FileWriter
from app.file_io.application.dtos import ReaderConfigDTO, WriterConfigDTO
from app.file_io.application.services import ReaderWriterSelectorService


def test_select_writer():
    """
    Tests that the selector returns the correct writer instance based on a valid writer configuration.
    """
    writer_config = WriterConfigDTO(source="local", file_format="csv", engine="pandas")
    service = ReaderWriterSelectorService(
        readers={}, writers={"local": {"csv": {"pandas": FileWriter}}}
    )
    writer = service("writer", writer_config)
    assert writer == FileWriter


def test_invalid_configuration_missing_reader_key():
    """
    Tests that a ValueError is raised when the readers dictionary is missing the expected key.
    """
    reader_config = ReaderConfigDTO(source="local", file_format="csv", engine="pandas")
    service = ReaderWriterSelectorService(readers={}, writers={})
    with pytest.raises(ValueError, match="Invalid configuration:"):
        service("reader", reader_config)


def test_invalid_configuration_missing_writer_key():
    """
    Tests that a ValueError is raised when the writers dictionary is missing the expected key.
    """
    writer_config = WriterConfigDTO(source="local", file_format="csv", engine="pandas")
    service = ReaderWriterSelectorService(readers={}, writers={})
    with pytest.raises(ValueError, match="Invalid configuration:"):
        service("writer", writer_config)


def test_valid_reader_writer_selection():
    """
    Tests that valid configurations correctly select both the reader and writer instances.
    """
    reader_config = ReaderConfigDTO(source="local", file_format="csv", engine="pandas")
    writer_config = WriterConfigDTO(source="local", file_format="csv", engine="pandas")
    service = ReaderWriterSelectorService(
        readers={"local": {"csv": {"pandas": FileReader}}},
        writers={"local": {"csv": {"pandas": FileWriter}}},
    )
    reader = service("reader", reader_config)
    assert reader == FileReader
    writer = service("writer", writer_config)
    assert writer == FileWriter
