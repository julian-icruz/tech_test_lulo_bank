from abc import ABC, abstractmethod


class TVMazeExtractorPort(ABC):
    """
    Abstract base class for extracting data from the TVMaze API.

    This class defines the interface for fetching TV schedule data from the API.
    Concrete implementations must provide a way to make the request to the TVMaze API
    and return the response as a list of dictionaries.

    Methods:
        extract_schedule(date: str) -> List[Dict]: Fetches the TV schedule for the given date.
    """

    @abstractmethod
    def extract_schedule(self, date: str) -> list[dict]:
        """
        Fetches the TV schedule data for a given date from the TVMaze API.

        Args:
            date (str): The date in 'YYYY-MM-DD' format for which to fetch the schedule.

        Returns:
            List[Dict]: A list of dictionaries containing the schedule data from the API.

        Raises:
            ValueError: If the date format is incorrect or if the API request fails.
        """
        pass
