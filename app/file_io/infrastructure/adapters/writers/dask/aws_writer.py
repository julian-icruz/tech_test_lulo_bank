import pyarrow as pa
import pyarrow.parquet as pq
import dask.dataframe as dd

from io import BytesIO
from dataclasses import dataclass

from app.file_io.domain.ports import FileWriter
from app.file_io.infrastructure.adapters.writers import BaseS3Writer


@dataclass
class DaskParquetWriterToS3(BaseS3Writer, FileWriter):
    """
    Writes a Dask DataFrame to a Parquet file in AWS S3 (single file).

    Notes:
        - Converts the Dask DataFrame to a pandas DataFrame before writing,
            as Dask doesn’t support direct single-file BytesIO writing.
        - Recommended for small to medium-sized datasets.
    """

    def write(self, data: dd.DataFrame, path: str, **kwargs) -> None:
        if data.compute().shape[0] == 0:
            raise ValueError("Cannot write an empty DataFrame to a Parquet file.")

        bucket = self._get_bucket(kwargs)
        df_pandas = data.compute()

        buffer = BytesIO()
        table = pa.Table.from_pandas(df_pandas)
        pq.write_table(table, buffer, **kwargs)
        buffer.seek(0)

        self.s3.upload_bytes(bucket, path, buffer.getvalue())
