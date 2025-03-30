import polars as pl
import pandas as pd

from app.file_io.domain.ports import FileReader


class PolarsJSONReader(FileReader):
    """
    Reads a JSON file and converts it into a Polars DataFrame.

    This uses pandas as an intermediary step because Polars does not yet support reading JSON directly.

    Args:
        path (str): Path to the JSON file.
        **kwargs: Additional arguments passed to pandas.read_json.

    Returns:
        pl.DataFrame: The JSON content as a Polars DataFrame.
    """

    def read(self, path: str, **kwargs) -> pl.DataFrame:
        df = pd.read_json(path, **kwargs)
        return pl.from_pandas(df)
