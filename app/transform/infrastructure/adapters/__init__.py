from app.transform.infrastructure.adapters.report_generator import (
    ReportGeneratorAdapter,
)

from app.transform.infrastructure.adapters.pandas.pandas_profiling_adapter import (
    PandasProfiling,
)
from app.transform.infrastructure.adapters.polars.polars_profiling_adapter import (
    PolarsProfiling,
)
from app.transform.infrastructure.adapters.dask.dask_profiling_adapter import (
    DaskProfiling,
)

PANDAS_ADAPTERS = [
    PandasProfiling,
]

POLARS_ADAPTERTS = [
    PolarsProfiling,
]

DASK_ADAPTERS = [
    DaskProfiling,
]

__ALL__ = [
    PANDAS_ADAPTERS,
    POLARS_ADAPTERTS,
    DASK_ADAPTERS,
    ReportGeneratorAdapter,
]
