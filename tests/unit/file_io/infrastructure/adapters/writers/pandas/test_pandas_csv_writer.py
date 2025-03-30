import pandas as pd

from app.file_io.infrastructure.adapters.writers import PandasCSVWriter


def test_write_csv_creates_file_and_matches_content(sample_dataframe, tmp_path):
    """
    Writes a CSV file and verifies the contents match the input DataFrame (including index).
    """
    path = tmp_path / "test_output.csv"
    writer = PandasCSVWriter()
    writer.write(sample_dataframe, path)

    result = pd.read_csv(path, index_col=0)
    pd.testing.assert_frame_equal(result, sample_dataframe)


def test_write_csv_with_custom_separator(sample_dataframe, tmp_path):
    """
    Writes a CSV file with a custom separator and verifies the contents match the input DataFrame (including index).
    """
    path = tmp_path / "custom_sep.csv"
    writer = PandasCSVWriter()
    writer.write(sample_dataframe, path, sep="|")

    result = pd.read_csv(path, sep="|", index_col=0)
    pd.testing.assert_frame_equal(result, sample_dataframe)
