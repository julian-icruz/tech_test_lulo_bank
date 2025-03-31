import os

from dataclasses import dataclass
from typing import Any

from app.load.infrastructure.adapters import PostgresLoaderAdapter
from app.file_io.application.services import ReaderWriterSelectorService


@dataclass
class LoadOrchestrationService:
    """
    Service to orchestrate the data loading process.

    Attributes:
        reader_writer_selector: Service to select the appropriate reader (from file_io).
        data_loader_adapter: Adapter implementing DataLoaderPort for inserting data.
    """

    reader_writer_selector: ReaderWriterSelectorService
    data_loader_adapter: PostgresLoaderAdapter

    def __call__(self, path_io: Any, reader_config: Any, model_class: Any) -> int:
        """
        Orchestrates the data loading process:
            1. Lists the Parquet files in the specified directory.
            2. Uses the selected reader to read each file.
            3. Inserts the read records into the database using the adapter.

        Args:
            path_io: DTO containing the input_path (directory of files).
            reader_config: Configuration used to select the reader.
            model_class: ORM model class representing the target table (e.g., Show, Episode, etc).

        Returns:
            int: Total number of records inserted.
        """
        self.data_loader_adapter.db_service.select_connector("postgres")

        file_reader = self.reader_writer_selector("reader", reader_config)
        total_records = 0

        for filename in os.listdir(path_io.input_path):
            if filename.endswith(".parquet"):
                file_path = os.path.join(path_io.input_path, filename)
                records = file_reader.read(file_path)
                total_records += len(records)
                self.data_loader_adapter.load_data(records, model_class)

        return total_records
