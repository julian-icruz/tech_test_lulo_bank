import json
import pandas as pd

from app.file_io.infrastructure.adapters.writers import PandasJSONWriter


def test_write_json_creates_file_and_matches_content(sample_dataframe, tmp_path):
    """
    Writes a DataFrame to JSON and validates content matches the original.
    """
    path = tmp_path / "data.json"
    writer = PandasJSONWriter()
    writer.write(sample_dataframe, path)

    result = pd.read_json(path)
    pd.testing.assert_frame_equal(result, sample_dataframe)


def test_write_json_orient_records(tmp_path):
    """
    Writes a DataFrame using 'records' orient and verifies structure.
    """
    df = pd.DataFrame([{"x": 1, "y": 2}, {"x": 3, "y": 4}])
    path = tmp_path / "records.json"
    writer = PandasJSONWriter()
    writer.write(df, path, orient="records")

    with open(path) as f:
        content = json.load(f)

    assert isinstance(content, list)
    assert content[0]["x"] == 1
