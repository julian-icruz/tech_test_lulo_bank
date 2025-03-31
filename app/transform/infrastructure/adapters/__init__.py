from app.transform.infrastructure.adapters.report_generator import (
    ReportGeneratorAdapter,
)

from app.transform.infrastructure.adapters.pandas.pandas_profiling_adapter import (
    PandasProfiling,
)
from app.transform.infrastructure.adapters.pandas.pandas_transformation_adapter import (
    PandasTransformation,
)

from app.transform.infrastructure.adapters.polars.polars_profiling_adapter import (
    PolarsProfiling,
)
from app.transform.infrastructure.adapters.polars.polars_transformation_adapter import (
    PolarsTransformation,
)

from app.transform.infrastructure.adapters.dask.dask_profiling_adapter import (
    DaskProfiling,
)
from app.transform.infrastructure.adapters.dask.dask_transformation_adapter import (
    DaskTransformation,
)

PANDAS_ADAPTERS = [
    PandasProfiling,
    PandasTransformation,
]

POLARS_ADAPTERTS = [
    PolarsProfiling,
    PolarsTransformation,
]

DASK_ADAPTERS = [
    DaskProfiling,
    DaskTransformation,
]

__ALL__ = [
    PANDAS_ADAPTERS,
    POLARS_ADAPTERTS,
    DASK_ADAPTERS,
    ReportGeneratorAdapter,
]
