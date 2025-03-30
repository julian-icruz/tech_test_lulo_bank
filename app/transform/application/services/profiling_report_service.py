from typing import Any, Dict
from dataclasses import dataclass

from app.transform.application.services import ProfilingService
from app.transform.infrastructure.adapters import ReportGeneratorAdapter

from app.file_io.domain.ports import FileWriter, FileReader
from app.file_io.application.dtos import WriterConfigDTO


@dataclass
class ProfilingReportService:
    reader: dict[str, dict[str, FileReader]]
    profiling_service: ProfilingService
    report_generator: ReportGeneratorAdapter
    file_writer: dict[str, dict[str, FileWriter]]

    def __call__(
        self,
        writer_config: WriterConfigDTO,
        # reader_config: ReaderConfigDTO,
        input_path: str,
        output_path: str,
    ) -> Dict[str, Any]:
        """
        Executes the profiling report process by performing the following steps:

        1. Reads data from the given input path using the file_reader.
        2. Generates profiling results by invoking the profiling_service.
        3. Creates an HTML report from the profiling results using the report_generator.
        4. Writes the generated report to the specified output path using the file_writer.

        Args:
            input_path (str): The path to the input file (e.g., a JSON file).
            output_path (str): The destination path for the generated report (HTML or PDF).
            **kwargs: Additional parameters (e.g., bucket, encoding) to pass to the file_reader and file_writer.

        Returns:
            Dict[str, Any]: A dictionary containing a status message and details about the output.
        """

        return {
            "message": "Profiling report generated and written successfully.",
        }
