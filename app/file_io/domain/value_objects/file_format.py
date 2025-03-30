from enum import Enum


class FileFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    YAML = "yaml"
    HTML = "html"
    PDF = "pdf"
