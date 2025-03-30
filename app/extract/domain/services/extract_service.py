from typing import List, Dict
from app.extract.domain.ports.tvmaze_extractor import TVMazeExtractor


class ExtractService:
    """
    Service layer that handles the logic of extracting data from the TVMaze API.

    This service interacts with the TVMazeExtractor to fetch TV schedule data for a specific date.
    It delegates the actual extraction logic to the TVMazeExtractor implementation and processes the data
    as needed (e.g., formatting or validation).

    Methods:
        get_schedule(date: str) -> List[Dict]: Fetches and returns the TV schedule for the given date.
    """

    def __init__(self, extractor: TVMazeExtractor) -> None:
        """
        Initializes the ExtractService with a specific TVMazeExtractor.

        Args:
            extractor (TVMazeExtractor): The TVMazeExtractor implementation to be used for fetching data.
        """
        self.extractor = extractor

    def get_schedule(self, date: str) -> List[Dict]:
        """
        Fetches the TV schedule for a given date by calling the extractor.

        Args:
            date (str): The date in 'YYYY-MM-DD' format for which to fetch the schedule.

        Returns:
            List[Dict]: A list of dictionaries containing the TV schedule data.

        Raises:
            ValueError: If the date format is incorrect or if the extraction fails.
        """
        return self.extractor.extract_schedule(date)
