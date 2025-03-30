import pytest

from app.file_io.container import FileIOContainer
from app.file_io.infrastructure.clients import S3Adapter


@pytest.fixture
def container():
    """Provides a fresh instance of FileIOContainer."""
    return FileIOContainer()


def test_container_provides_local_csv_pandas_reader(container):
    reader = container.readers()["local"]["csv"]["pandas"]
    assert reader.__class__.__name__ == "PandasCSVReader"


def test_container_provides_local_json_json_reader(container):
    reader = container.readers()["local"]["json"]["json"]
    assert reader.__class__.__name__ == "JSONReader"


def test_container_provides_aws_json_pandas_reader(container):
    reader = container.readers()["aws"]["json"]["pandas"]
    assert reader.__class__.__name__ == "PandasJSONReaderFromS3"
    assert isinstance(reader.s3, S3Adapter)


def test_container_provides_local_parquet_polars_writer(container):
    writer = container.writers()["local"]["parquet"]["polars"]
    assert writer.__class__.__name__ == "PolarsParquetWriter"


def test_container_provides_aws_pdf_writer(container):
    writer = container.writers()["aws"]["pdf"]["pdf"]
    assert writer.__class__.__name__ == "PDFWriterToS3"
    assert isinstance(writer.s3, S3Adapter)


def test_container_s3_adapter_is_singleton(container):
    reader1 = container.readers()["aws"]["csv"]["pandas"]
    writer1 = container.writers()["aws"]["csv"]["pandas"]
    assert reader1.s3 is writer1.s3
