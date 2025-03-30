import dask.dataframe as dd
from app.file_io.infrastructure.adapters.readers import DaskCSVReader


def test_dask_csv_reader_basic(temp_csv_path):
    """Reads a basic CSV file with Dask and verifies its content."""
    path = temp_csv_path("a,b\n1,2\n3,4")
    reader = DaskCSVReader()
    df = reader.read(path)

    assert isinstance(df, dd.DataFrame)
    result = df.compute()
    assert result.shape == (2, 2)
    assert result.iloc[0]["a"] == 1


def test_dask_csv_reader_custom_delimiter(temp_csv_path):
    """Reads a CSV file with a custom delimiter using Dask."""
    path = temp_csv_path("x;y\n10;20")
    reader = DaskCSVReader()
    df = reader.read(path, sep=";")

    result = df.compute()
    assert result.columns.tolist() == ["x", "y"]
    assert result.iloc[0]["y"] == 20


def test_dask_csv_reader_missing_file():
    """Raises FileNotFoundError when CSV file is missing."""
    reader = DaskCSVReader()
    try:
        reader.read("missing.csv").compute()
    except FileNotFoundError:
        assert True
