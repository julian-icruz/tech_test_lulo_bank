import os
import ast
import pandas as pd
import numpy as np
from dataclasses import dataclass

from app.load.domain.models import Show, Episode, WebChannel
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

        paths_suffix = ["shows", "episodes", "web_channel"]
        dfs_list = []

        for suffix in paths_suffix:
            path = os.path.join(path_io.input_path, suffix)
            dfs_list.append(file_reader.read(path))

        df_shows = dfs_list[0]
        df_episodes = dfs_list[1]
        df_web_channel = dfs_list[2]

        df_shows.rename(columns={"id_1": "web_channel_id"}, inplace=True)
        df_shows["updated"] = pd.to_datetime(df_shows["updated"], errors="coerce")

        df_shows = df_shows.where(pd.notnull(df_shows), None)
        df_episodes = df_episodes.where(pd.notnull(df_episodes), None)
        df_web_channel = df_web_channel.where(pd.notnull(df_web_channel), None)

        columns = [
            "id",
            "averageRuntime",
            "weight",
            "thetvdb",
            "runtime",
            "id_2",
            "tvrage",
        ]

        df_shows[columns] = df_shows[columns].apply(pd.to_numeric, errors="coerce")
        df_shows[columns] = df_shows[columns].astype("Int64")
        df_shows = df_shows.replace({pd.NA: None, np.nan: None})
        df_shows["genres"] = df_shows["genres"].apply(lambda x: ast.literal_eval(x))

        columns = ["id", "season", "number", "runtime", "show_id"]
        df_episodes[columns] = df_episodes[columns].apply(
            pd.to_numeric, errors="coerce"
        )
        df_episodes[columns] = df_episodes[columns].astype("Int64")
        df_episodes = df_episodes.replace({pd.NA: None, np.nan: None})
        df_episodes["airtime"] = df_episodes["airtime"].replace("", None)

        shows_data = df_shows.to_dict(orient="records")
        episodes_data = df_episodes.to_dict(orient="records")
        web_channel_data = df_web_channel.to_dict(orient="records")

        self.data_loader_adapter.load_data(web_channel_data, WebChannel)
        self.data_loader_adapter.load_data(shows_data, Show)
        self.data_loader_adapter.load_data(episodes_data, Episode)
        return
