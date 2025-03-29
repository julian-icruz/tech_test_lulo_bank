import pandas as pd
from app.file_io.infrastructure.adapters.readers import PandasCSVReader


def test_pandas_csv_reader_reads_file_correctly(csv_file_path):
    """
    Test that PandasCSVReader correctly reads a CSV file and returns a DataFrame
    with the expected content and structure.
    """
    reader = PandasCSVReader()

    df = reader.read(csv_file_path)

    expected_df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    pd.testing.assert_frame_equal(df, expected_df)
