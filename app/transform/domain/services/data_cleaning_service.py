from typing import Any

from app.transform.domain.services import BaseTransformService


class DataCleaningService(BaseTransformService):

    def __call__(self, data: Any) -> dict[str, Any]:
        """
        Orchestrates the data profiling process by invoking methods from the data profiling adapter.

        Args:
            data (Any): Input data (e.g., a DataFrame from pandas, polars, or dask).

        Returns:
            Dict[str, Any]: A dictionary containing profiling results including descriptive statistics,
                            missing values, duplicates, correlations, and column type profiles.
        """
        data_flattened_show = []
        data_flattened_episodes = []

        for df in data:
            data_flattened_show.append(self.transformation_adapter.flatten_show(df))
            data_flattened_episodes.append(
                self.transformation_adapter.flatten_episodes(df)
            )

        list_df_show_filtered = (
            self.transformation_adapter.filter_and_clean_empty_columns(
                data_flattened_show
            )
        )

        data_show_merged = self.transformation_adapter.merge_dataframes(
            list_df_show_filtered
        )
        data_episodes_merged = self.transformation_adapter.merge_dataframes(
            data_flattened_episodes
        )

        df_shows = (
            self.transformation_adapter.convert_lists_to_strings_and_drop_duplicates(
                data_show_merged
            )
        )

        df_episodes = self.transformation_adapter.clean_episode_duplicates(
            data_episodes_merged
        )

        df_shows, df_web_channel = self.transformation_adapter.get_df_web_channel(
            df_shows
        )

        df_shows = self.transformation_adapter.rename_columns(df_shows)
        df_web_channel = self.transformation_adapter.rename_columns(df_web_channel)

        return df_shows, df_episodes, df_web_channel
