import os
from dataclasses import dataclass

from app.file_io.domain.ports import FileWriter
from app.extract.domain.services import ExtractService

from app.file_io.application.dtos import WriterConfigDTO


@dataclass
class ExtractStorageService:
    """
    ExtractStorageService fetches TV schedule data for a specified date using an extraction service and stores
    each schedule entry as a JSON file in a hive-partitioned directory structure. Each file is named using the
    schedule entry's 'id'. The service selects the appropriate file writer based on the provided source, file format,
    and engine parameters.

    Attributes:
        extract_service (ExtractService): The service used to extract TV schedule data.
        writers (dict): A nested dictionary of file writer providers.
    """

    extract_service: ExtractService
    writers: dict[str, dict[str, FileWriter]]

    async def extract_and_store(
        self,
        date: str,
        writer_config: WriterConfigDTO,
        storage_folder: str = "json",
    ) -> None:
        """
        Extracts TV schedule data for the specified date and stores each schedule entry as a file.
        The files are saved in a subdirectory formatted as '{storage_folder}/date={date}'.

        Parameters:
            date (str): The schedule date in 'YYYY-MM-DD' format.
            source (str): The key representing the storage source (e.g., "local" or "aws").
            file_format (str): The file format to use for storing data (e.g., "json").
            engine (str): The specific writer engine to utilize (e.g., "json" for built-in JSON writer).
            storage_folder (str): The base directory where files will be stored (default is "json").

        Raises:
            ValueError: If the specified writer configuration does not exist.
        """
        partition_folder = f"{storage_folder}/date={date}"
        os.makedirs(partition_folder, exist_ok=True)
        schedule = await self.extract_service.get_schedule(date)

        source = writer_config.source
        file_format = writer_config.file_format
        engine = writer_config.engine

        try:
            writer_provider = self.writers()[source][file_format][engine]
        except KeyError as e:
            raise ValueError(f"Invalid writer configuration: {e}")
        for item in schedule:
            file_id = item.get("id")
            if not file_id:
                continue
            file_path = (
                f"{partition_folder}/{file_id}.{writer_config.file_format.value}"
            )
            writer_provider.write(item, file_path, indent=4)
        return len(schedule)
