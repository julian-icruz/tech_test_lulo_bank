import pytest
import pandas as pd
import dask.dataframe as dd

from app.file_io.infrastructure.adapters.writers import DaskParquetWriter


def test_dask_parquet_writer(sample_dataframe, tmp_path):
    """
    Verifies that DaskParquetWriter correctly writes a Parquet file to the local filesystem.
    """
    dask_df = dd.from_pandas(sample_dataframe, npartitions=1)
    writer = DaskParquetWriter()
    path = tmp_path / "test_output.parquet"
    writer.write(dask_df, path)
    result = dd.read_parquet(path)
    assert result.compute().equals(dask_df.compute())


def test_dask_parquet_writer_empty_dataframe(tmp_path):
    """
    Verifica que DaskParquetWriter lance un error al intentar escribir un archivo Parquet vacío.
    """
    empty_df = dd.from_pandas(pd.DataFrame(columns=["col1", "col2"]), npartitions=1)
    writer = DaskParquetWriter()
    path = tmp_path / "empty_output.parquet"

    with pytest.raises(ValueError):
        writer.write(empty_df, path)
