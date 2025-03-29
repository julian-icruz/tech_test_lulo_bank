from dependency_injector.providers import Dict, Factory
from dependency_injector.containers import DeclarativeContainer

from file_io.infrastructure.adapters.readers import (
    PandasCSVReader,
    PandasJSONReader,
    PandasParquetReader,
    PolarsCSVReader,
    PolarsParquetReader,
    DaskCSVReader,
    DaskParquetReader,
    JSONReader,
    YAMLReader,
)


class FileIOContainer(DeclarativeContainer):
    readers = Dict(
        csv=Dict(
            pandas=Factory(PandasCSVReader),
            polars=Factory(PolarsCSVReader),
            dask=Factory(DaskCSVReader),
        ),
        json=Dict(
            pandas=Factory(PandasJSONReader),
            structured=Factory(JSONReader),
        ),
        parquet=Dict(
            pandas=Factory(PandasParquetReader),
            polars=Factory(PolarsParquetReader),
            dask=Factory(DaskParquetReader),
        ),
        yaml=Factory(YAMLReader),
    )
