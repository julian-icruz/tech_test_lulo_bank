import os
import numpy as np
import pandas as pd
from dataclasses import dataclass

from app.load.domain.models import Show, Episode, WebChannel, Network
from app.load.infrastructure.adapters import PostgresLoaderAdapter

from app.file_io.application.dtos import ReaderConfigDTO, PathIODTO
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

    def __call__(
        self,
        path_io: PathIODTO,
        reader_config: ReaderConfigDTO,
        database: str = "postgres",
    ) -> int:
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
        self.data_loader_adapter.db_service.select_connector(database)

        file_reader = self.reader_writer_selector("reader", reader_config)

        paths_suffix = ["shows", "episodes", "web_channels", "networks"]
        dfs_list = []

        for suffix in paths_suffix:
            path = os.path.join(path_io.input_path, suffix)
            dfs_list.append(file_reader.read(path))

        df_shows = dfs_list[0]
        df_episodes = dfs_list[1]
        df_web_channel = dfs_list[2]
        df_networks = dfs_list[3]

        numeric_columns_shows = ["id", "thetvdb", "tvrage"]
        df_shows = self.normalize_numeric_columns(df_shows, numeric_columns_shows)

        numeric_columns_episodes = ["id", "season", "number", "runtime", "show_id"]
        df_episodes = self.normalize_numeric_columns(
            df_episodes, numeric_columns_episodes
        )

        shows_data = df_shows.to_dict(orient="records")
        episodes_data = df_episodes.to_dict(orient="records")
        web_channel_data = df_web_channel.to_dict(orient="records")
        networks_data = df_networks.to_dict(orient="records")

        self.data_loader_adapter.load_data(web_channel_data, WebChannel)
        self.data_loader_adapter.load_data(networks_data, Network)
        self.data_loader_adapter.load_data(shows_data, Show)
        self.data_loader_adapter.load_data(episodes_data, Episode)
        return

    def normalize_numeric_columns(
        self, data: pd.DataFrame, numeric_columns: list
    ) -> pd.DataFrame:
        """
        Normalize numeric columns in the DataFrame to handle NaN values.
        Args:
            data (pd.DataFrame): DataFrame containing the data to be normalized.
            numeric_columns (list): List of column names to be normalized.
        Returns:
            pd.DataFrame: DataFrame with normalized numeric columns.
        """
        data[numeric_columns] = data[numeric_columns].apply(
            pd.to_numeric, errors="coerce"
        )
        data[numeric_columns] = data[numeric_columns].astype("Int64")
        data = data.replace({pd.NA: None, np.nan: None})
        return data
