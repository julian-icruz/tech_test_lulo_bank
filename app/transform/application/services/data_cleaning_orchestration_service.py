import os
from typing import Any
from dataclasses import dataclass

from app.transform.domain.services import DataCleaningService

from app.file_io.application.services import ReaderWriterSelectorService
from app.file_io.application.dtos import WriterConfigDTO, ReaderConfigDTO, PathIODTO


@dataclass
class DataCleaninOrchestrationService:
    data_cleaning_service: DataCleaningService
    reader_writer_selector: ReaderWriterSelectorService

    def __call__(
        self,
        writer_config: WriterConfigDTO,
        reader_config: ReaderConfigDTO,
        path_io: PathIODTO,
    ) -> dict[str, Any]:
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
            dict[str, Any]: A dictionary containing a status message and details about the input and output paths.
        """
        try:
            files = os.listdir(path_io.input_path)
        except Exception as e:
            raise Exception(f"Error listing files in {path_io.input_path}: {str(e)}")

        data_list = []
        file_reader = self.reader_writer_selector("reader", reader_config)
        for file in files:
            file_path = os.path.join(path_io.input_path, file)
            if file.endswith(reader_config.file_format):
                data_list.append(file_reader.read(file_path))

        self.data_cleaning_service._select_adapter(reader_config.engine)
        data_shows, data_episodes, data_web_channel = self.data_cleaning_service(
            data_list
        )

        path_shows = path_io.output_path + "shows/"
        path_episodes = path_io.output_path + "episodes/"
        path_web_channel = path_io.output_path + "web_channel/"

        os.makedirs(path_shows, exist_ok=True)
        os.makedirs(path_episodes, exist_ok=True)
        os.makedirs(path_web_channel, exist_ok=True)

        file_writer = self.reader_writer_selector("writer", writer_config)
        file_writer.write(
            data_shows,
            path_shows + "data.snappy.parquet",
            compression="snappy",
            engine="pyarrow",
        )

        file_writer.write(
            data_episodes,
            path_episodes + "data.snappy.parquet",
            compression="snappy",
            engine="pyarrow",
        )

        file_writer.write(
            data_web_channel,
            path_web_channel + "data.snappy.parquet",
            compression="snappy",
            engine="pyarrow",
        )

        return
