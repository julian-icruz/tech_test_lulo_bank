import pytest
import polars as pl

from app.file_io.infrastructure.adapters.readers import PolarsJSONReader


def test_polars_json_reader_valid_file(temp_json_path):
    """
    Reads a valid JSON file and verifies that a Polars DataFrame is returned with correct shape and content.
    """
    path = temp_json_path('[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')
    reader = PolarsJSONReader()
    df = reader.read(path)

    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 2)
    assert df[0, "name"] == "Alice"


def test_polars_json_reader_missing_field(temp_json_path):
    """
    Reads a JSON file with inconsistent fields and ensures NaN handling.
    """
    path = temp_json_path('[{"a": 1}, {"a": 2, "b": 3}]')
    reader = PolarsJSONReader()
    df = reader.read(path)

    assert df.shape == (2, 2)
    assert df[0, "b"] is None


def test_polars_json_reader_empty_file(temp_json_path):
    """
    Ensures that reading an empty JSON file raises an appropriate exception.
    """
    path = temp_json_path("")
    reader = PolarsJSONReader()
    with pytest.raises(Exception):
        reader.read(path)


def test_polars_json_reader_malformed_json(temp_json_path):
    """
    Ensures that malformed JSON input raises an exception.
    """
    path = temp_json_path('[{"a": 1}, {"a": 2}')
    reader = PolarsJSONReader()
    with pytest.raises(Exception):
        reader.read(path)
