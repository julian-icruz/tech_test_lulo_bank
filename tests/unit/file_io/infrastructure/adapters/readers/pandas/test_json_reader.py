import pytest
import pandas as pd

from app.file_io.infrastructure.adapters.readers import PandasJSONReader


def test_read_valid_json_file(temp_json_path):
    """Reads a valid JSON file and checks if the DataFrame is correctly loaded."""
    path = temp_json_path('[{"col1": 1, "col2": 2}, {"col1": 3, "col2": 4}]')
    reader = PandasJSONReader()
    df = reader.read(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.iloc[0]["col1"] == 1


def test_read_json_file_with_missing_fields(temp_json_path):
    """Reads a JSON file with missing fields in some objects and verifies DataFrame is loaded with NaNs."""
    path = temp_json_path('[{"col1": 1}, {"col1": 2, "col2": 3}]')
    reader = PandasJSONReader()
    df = reader.read(path)
    assert df.shape == (2, 2)
    assert pd.isna(df.iloc[0]["col2"])


def test_read_empty_json_file(temp_json_path):
    """Checks that reading an empty JSON file raises a ValueError."""
    path = temp_json_path("")
    reader = PandasJSONReader()
    with pytest.raises(ValueError):
        reader.read(path)


def test_read_malformed_json_file(temp_json_path):
    """Checks that reading a malformed JSON raises a ValueError."""
    path = temp_json_path(
        '[{"col1": 1, "col2": 2}, {"col1": 3, "col2": 4}'
    )  # Missing closing brace
    reader = PandasJSONReader()
    with pytest.raises(ValueError):
        reader.read(path)
