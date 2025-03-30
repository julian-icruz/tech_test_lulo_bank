from dataclasses import dataclass

from app.extract.domain.ports.tvmaze_extractor import TVMazeExtractorPort


@dataclass
class ExtractService:
    """
    Service layer that handles the logic of extracting data from the TVMaze API.

    This service interacts with the TVMazeExtractorPort to fetch TV schedule data for a specific date.
    It delegates the actual extraction logic to the TVMazeExtractorPort implementation and processes the data
    as needed (e.g., formatting or validation).

    Methods:
        get_schedule(date: str) -> list[dict]: Fetches and returns the TV schedule for the given date.
    """

    extractor_adapter: TVMazeExtractorPort

    def get_schedule(self, date: str) -> list[dict]:
        """
        Fetches the TV schedule for a given date by calling the extractor.

        Args:
            date (str): The date in 'YYYY-MM-DD' format for which to fetch the schedule.

        Returns:
            list[dict]: A list of dictionaries containing the TV schedule data.

        Raises:
            ValueError: If the date format is incorrect or if the extraction fails.
        """
        return self.extractor_adapter.extract_schedule(date)
