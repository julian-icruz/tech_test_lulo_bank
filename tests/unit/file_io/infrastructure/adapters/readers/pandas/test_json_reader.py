from app.file_io.infrastructure.adapters.readers import JSONReader


def test_json_reader_reads_file_correctly(json_file_path):
    """
    Test that JSONReader reads a local JSON file correctly
    and returns the expected data structure.
    """
    reader = JSONReader()

    result = reader.read(json_file_path)

    expected = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    assert result == expected
