import polars as pl
import pandas as pd

from app.file_io.infrastructure.adapters.writers import PolarsCSVWriter


def test_write_polars_csv_creates_file_and_matches_content(tmp_path):
    """
    Writes a Polars DataFrame to a CSV file and verifies the file content matches the original.
    """
    df = pl.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    path = tmp_path / "output.csv"

    writer = PolarsCSVWriter()
    writer.write(df, path)

    result = pd.read_csv(path)
    expected = df.to_pandas()

    pd.testing.assert_frame_equal(result, expected)


def test_write_polars_csv_with_custom_separator(tmp_path):
    """
    Writes a Polars DataFrame to a CSV file using a custom separator and verifies correctness.
    """
    df = pl.DataFrame({"x": [10, 20], "y": ["foo", "bar"]})
    path = tmp_path / "output_sep.csv"

    writer = PolarsCSVWriter()
    writer.write(df, path, separator="|")

    result = pd.read_csv(path, sep="|")
    expected = df.to_pandas()

    pd.testing.assert_frame_equal(result, expected)
