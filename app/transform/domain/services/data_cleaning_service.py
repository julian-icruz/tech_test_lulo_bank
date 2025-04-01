from typing import Any

from app.transform.domain.services import BaseTransformService


class DataCleaningService(BaseTransformService):

    def __call__(self, data: Any) -> dict[str, Any]:
        """
        Orchestrates the data cleaning process:
            1. Flattens nested structures in the data.
            2. Filters and cleans empty columns.
            3. Merges DataFrames.
            4. Processes shows and episodes: converts lists to strings and removes duplicates.
            5. Extracts DataFrames for web_channel and networks.
            6. Renames columns in all DataFrames.
            7. Converts date/time columns.
            8. Replaces NaN values with None.
            9. Normalizes numeric columns.
            10. Evaluates literal columns.
            11. Replaces empty strings with None.
        Args:
            data (Any): List of DataFrames to be processed.
        Returns:
            dict[str, Any]: A dictionary containing processed DataFrames for shows, episodes, web_channel, and networks.
        """
        flattened_shows = [self.transformation_adapter.flatten_show(df) for df in data]
        flattened_episodes = [
            self.transformation_adapter.flatten_episodes(df) for df in data
        ]

        filtered_shows = self.transformation_adapter.filter_and_clean_empty_columns(
            flattened_shows
        )

        merged_shows = self.transformation_adapter.merge_dataframes(filtered_shows)
        merged_episodes = self.transformation_adapter.merge_dataframes(
            flattened_episodes
        )

        df_shows = (
            self.transformation_adapter.convert_lists_to_strings_and_drop_duplicates(
                merged_shows
            )
        )
        df_episodes = self.transformation_adapter.clean_episode_duplicates(
            merged_episodes
        )

        df_shows, df_web_channel, df_networks = self.transformation_adapter.get_sub_dfs(
            df_shows
        )

        df_shows = self.transformation_adapter.rename_columns(df_shows)
        df_web_channel = self.transformation_adapter.rename_columns(
            df_web_channel, False
        )
        df_networks = self.transformation_adapter.rename_columns(df_networks, False)

        df_shows = self.transformation_adapter.convert_date_time_columns(
            df_shows, "updated"
        )

        df_shows = self.transformation_adapter.replace_nan_with_none(df_shows)
        df_episodes = self.transformation_adapter.replace_nan_with_none(df_episodes)
        df_web_channel = self.transformation_adapter.replace_nan_with_none(
            df_web_channel
        )
        df_networks = self.transformation_adapter.replace_nan_with_none(df_networks)

        columns_show = [
            "id",
            "averageruntime",
            "weight",
            "thetvdb",
            "runtime",
            "network_id",
            "webchannel_id",
            "tvrage",
        ]
        df_shows = self.transformation_adapter.normalize_columns(df_shows, columns_show)

        columns_episodes = ["id", "season", "number", "runtime", "show_id"]
        df_episodes = self.transformation_adapter.normalize_columns(
            df_episodes, columns_episodes
        )

        df_shows = self.transformation_adapter.evaluate_literal_column(
            df_shows, "genres"
        )
        df_shows = self.transformation_adapter.evaluate_literal_column(df_shows, "days")

        df_episodes = self.transformation_adapter.replace_empty_with_none(
            df_episodes, "airtime"
        )

        return df_shows, df_episodes, df_web_channel, df_networks
