from pydantic import BaseModel


class PathIODTO(BaseModel):
    """
    DTO that encapsulates I/O path configuration for data processing.

    Attributes:
        input_path (str | None): The file path from which to read input data. Defaults to None.
        output_path (str | None): The file path where the processed data or report will be written. Defaults to None.
        bucket (str | None): Optional storage bucket identifier, used for cloud storage configurations. Defaults to None.
    """

    input_path: str | None = None
    output_path: str | None = None
    bucket: str | None = None
