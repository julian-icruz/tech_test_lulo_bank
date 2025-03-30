import pytest
import pandas as pd

from app.file_io.infrastructure.adapters.readers import PandasCSVReader


def test_read_csv_basic(temp_csv_path):
    """Reads a basic CSV file with headers and verifies the shape and column names."""
    path = temp_csv_path("col1,col2\n1,2\n3,4")
    reader = PandasCSVReader()
    df = reader.read(path)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["col1", "col2"]


def test_read_csv_without_header(temp_csv_path):
    """Reads a CSV file without headers and checks default column names as integers."""
    path = temp_csv_path("1,2,3\n4,5,6")
    reader = PandasCSVReader()
    df = reader.read(path, header=None)
    assert df.shape == (2, 3)
    assert list(df.columns) == [0, 1, 2]


def test_read_csv_with_custom_delimiter(temp_csv_path):
    """Reads a CSV file using a custom delimiter and verifies correct parsing."""
    path = temp_csv_path("a;b;c\n1;2;3")
    reader = PandasCSVReader()
    df = reader.read(path, sep=";")
    assert df.columns.tolist() == ["a", "b", "c"]
    assert df.iloc[0]["b"] == 2


def test_read_nonexistent_file():
    """Checks that reading a non-existent file raises a FileNotFoundError."""
    reader = PandasCSVReader()
    with pytest.raises(FileNotFoundError):
        reader.read("non_existent_file.csv")


def test_read_empty_csv(temp_csv_path):
    """Checks that reading an empty CSV file raises a pandas EmptyDataError."""
    path = temp_csv_path("")
    reader = PandasCSVReader()
    with pytest.raises(pd.errors.EmptyDataError):
        reader.read(path)
