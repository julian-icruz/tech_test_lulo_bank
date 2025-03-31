import os
from typing import Any, Dict
from dataclasses import dataclass

from app.transform.application.services import ProfilingService
from app.transform.infrastructure.adapters import ReportGeneratorAdapter

from app.file_io.application.services import ReaderWriterSelectorService
from app.file_io.application.dtos import WriterConfigDTO, ReaderConfigDTO, PathIODTO


@dataclass
class ProfilingReportService:
    profiling_service: ProfilingService
    report_generator: ReportGeneratorAdapter
    reader_writer_selector: ReaderWriterSelectorService

    def __call__(
        self,
        writer_config: WriterConfigDTO,
        reader_config: ReaderConfigDTO,
        path_io: PathIODTO,
    ) -> Dict[str, Any]:
        """
        Executes the complete profiling report process by performing the following steps:

        1. Reads data from the specified input path using the selected file reader.
        2. Generates profiling results by invoking the profiling servicea.
        3. Creates an HTML report from the profiling results using the report generator adapter.
        4. Ensures the output directory exists and writes the generated report using the selected file writer.

        Args:
            writer_config (WriterConfigDTO): Configuration for file writing (source, file format, engine).
            reader_config (ReaderConfigDTO): Configuration for file reading (source, file format, engine).
            path_io (PathIODTO): DTO containing input_path, output_path, and optional bucket for storage.

        Returns:
            Dict[str, Any]: A dictionary containing a status message and details about the input and output paths.
        """
        file_reader = self.reader_writer_selector("reader", reader_config)
        data = file_reader.read(path_io.input_path, bucket=path_io.bucket)

        profiling_results = self.profiling_service.profile(data)
        report_content = self.report_generator.generate_report(profiling_results)

        output_dir = os.path.dirname(path_io.output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        file_writer = self.reader_writer_selector("writer", writer_config)
        file_writer.write(report_content, path_io.output_path, bucket=path_io.bucket)

        return {
            "message": "Profiling report generated and written successfully.",
            "input": path_io.input_path,
            "output": path_io.output_path,
        }
