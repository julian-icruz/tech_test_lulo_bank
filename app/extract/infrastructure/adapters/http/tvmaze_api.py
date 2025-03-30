import httpx

from app.extract.domain.ports import TVMazeExtractorPort


class TVMazeAPIAdapter(TVMazeExtractorPort):
    """
    Adapter for interacting with the TVMaze API to fetch TV schedule data.

    Args:
        base_url (str): The base URL of the TVMaze API.
        client (httpx.AsyncClient): HTTP client for making requests to the API.

    Methods:
        fetch_schedule(date: str) -> list[dict]: Fetches the TV schedule for the given date from the TVMaze API.
    """

    def __init__(
        self, base_url: str = "http://api.tvmaze.com", client: httpx.AsyncClient = None
    ):
        """
        Initializes the TVMaze API client.

        Args:
            base_url (str): The base URL for the API (default: "http://api.tvmaze.com").
            client (httpx.AsyncClient): Optional HTTP client for custom request handling.
        """
        self.base_url = base_url
        self.client = client or httpx.AsyncClient()

    async def extract_schedule(self, date: str) -> list[dict]:
        """
        Fetches the TV schedule for the specified date from the TVMaze API.

        Args:
            date (str): The date for which the TV schedule is to be fetched (format: "YYYY-MM-DD").

        Returns:
            list[dict]: A list of dictionaries containing TV schedule data.
        """
        url = f"{self.base_url}/schedule/web"
        params = {"date": date}

        try:
            response = await self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except httpx.RequestError as e:
            raise Exception(f"Request error occurred: {e}")
