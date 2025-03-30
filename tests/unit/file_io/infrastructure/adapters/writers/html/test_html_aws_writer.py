from app.file_io.infrastructure.adapters.writers import HTMLWriter


def test_html_writer_writes_basic_html(tmp_path):
    """
    Writes a basic HTML string to a file and verifies its contents.
    """
    content = "<html><body><h1>Hello World</h1></body></html>"
    output_path = tmp_path / "basic.html"

    writer = HTMLWriter()
    writer.write(content, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()

    assert content in result


def test_html_writer_with_unicode(tmp_path):
    """
    Writes an HTML file with unicode characters and verifies encoding.
    """
    content = "<p>Python 🐍 is fun!</p>"
    output_path = tmp_path / "emoji.html"

    writer = HTMLWriter()
    writer.write(content, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()

    assert "🐍" in result
