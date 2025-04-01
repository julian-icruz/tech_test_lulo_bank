from enum import Enum


class WriterEngine(str, Enum):
    # For JSON: "pandas", "json"
    PANDAS = "pandas"
    JSON = "json"
    # For Parquet: "pandas", "polars", "dask"
    POLARS = "polars"
    DASK = "dask"
    # For YAML, HTML y PDF, según corresponda
    YAML = "yaml"
    HTML = "html"
    PDFKIT = "pdfkit"
    WEASYPRINT = "weasyprint"
