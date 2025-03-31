import pandas as pd
from typing import Any, List
from dataclasses import dataclass

from app.transform.domain.ports import DataTransformationPort


@dataclass
class PandasTransformation(DataTransformationPort):
    def flatten_nested_structures(self, data: Any) -> Any:
        """
        Flattens nested structures in a pandas DataFrame.
        """
        return pd.json_normalize(data.to_dict(orient="records"), sep="_")

    def flatten_show(self, data: Any) -> Any:
        """
        Flattens the DataFrame and shows the first few rows for inspection.

        Args:
            data (Any): Input data (e.g., a pandas DataFrame).

        Returns:
            Any: The flattened DataFrame.
        """
        return pd.json_normalize(data["_embedded"]["show"], sep="_")

    def flatten_episodes(self, data: Any) -> Any:
        """
        Flattens the episodes data from the DataFrame.

        Args:
            data (Any): Input data (e.g., a pandas DataFrame).

        Returns:
            Any: The flattened DataFrame for episodes.
        """
        df_show = self.flatten_show(data)
        show_id = df_show["id"].values[0]
        df_episodes = data.drop(
            columns=["_embedded", "_links", "image"]
        ).drop_duplicates()
        df_episodes["show_id"] = show_id
        return df_episodes

    def filter_and_clean_empty_columns(self, list_df):
        """
        Filtra los DataFrames de la lista y elimina las columnas que estén completamente vacías.

        Parameters:
        - list_df: Lista de DataFrames

        Returns:
        - list_df_filtered: Lista de DataFrames filtrados con columnas no vacías
        """
        return [
            df.dropna(axis=1, how="all")
            for df in list_df
            if not df.dropna(how="all").empty
        ]

    def convert_lists_to_strings_and_drop_duplicates(self, df):
        """
        Convierte las listas en el DataFrame a cadenas de texto y elimina las filas duplicadas.

        Parameters:
        - df: DataFrame a limpiar.

        Returns:
        - df_cleaned: DataFrame después de convertir las listas a cadenas y eliminar duplicados.
        """
        df_cleaned = df.map(lambda x: str(x) if isinstance(x, list) else x)
        df_cleaned = df_cleaned.drop_duplicates()

        return df_cleaned

    def clean_episode_duplicates(self, df):
        """
        Elimina los duplicados por 'id' y maneja los casos con valores nulos en la columna 'rating'.

        - Los duplicados con 'rating' nulo se eliminan.
        - Se conserva solo uno de los duplicados con 'rating' no nulo.

        Parameters:
        - df: DataFrame de episodios con la columna 'id' y 'rating'.

        Returns:
        - df_cleaned: DataFrame limpio después de eliminar duplicados y manejar los valores nulos en 'rating'.
        """
        duplicated_ids = df[df.duplicated(subset="id", keep=False)]
        df_episode_cleaned_no_null_rating = duplicated_ids[
            duplicated_ids["rating"].notnull()
        ]
        df_episode_cleaned_final = df[
            ~df["id"].isin(df_episode_cleaned_no_null_rating["id"])
        ]
        df_cleaned = pd.concat(
            [df_episode_cleaned_final, df_episode_cleaned_no_null_rating],
            ignore_index=True,
        )
        return df_cleaned

    def get_df_web_channel(self, data: Any) -> Any:
        """
        Obtiene el DataFrame de la columna 'web_channel'.

        Args:
            data (Any): Input data (e.g., a pandas DataFrame).

        Returns:
            Any: The DataFrame for the 'web_channel' column.
        """

        webchannel_columns = [col for col in data.columns if "webChannel" in col]
        network_columns = [col for col in data.columns if "network" in col]
        webchannel_columns_to_drop = [
            col for col in webchannel_columns if col != "webChannel_id"
        ]
        network_columns_to_drop = [
            col for col in network_columns if col != "network_id"
        ]
        df_webchannel = data[webchannel_columns].drop_duplicates().dropna(how="all")
        df_network = data[network_columns].drop_duplicates().dropna(how="all")
        df_without = data.drop(
            columns=webchannel_columns_to_drop + network_columns_to_drop
        )
        return df_without, df_webchannel, df_network

    def rename_columns(self, data: Any) -> Any:
        """
        Renames columns in a pandas DataFrame.

        Args:
            data (Any): A pandas DataFrame.

        Returns:
            Any: The DataFrame with renamed columns.
        """
        data.columns = data.columns.str.lower()
        new_columns = {}
        seen = {}

        for col in data.columns:
            if col in ["network_id", "webchannel_id"]:
                new_columns[col] = col
                continue

            new_name = col.split("_", 1)[-1] if "_" in col else col

            if new_name in seen:
                seen[new_name] += 1
                new_name = f"{new_name}_{seen[new_name]}"
            else:
                seen[new_name] = 0

            new_columns[col] = new_name

        return data.rename(columns=new_columns)

    def convert_date_time_columns(self, data: Any) -> Any:
        pass

    def normalize_columns(self, data: Any) -> Any:
        pass

    def categorize_columns(self, data: Any) -> Any:
        pass

    def merge_dataframes(self, data_list: List[Any]) -> Any:
        """
        Merges a list of pandas DataFrames into a single DataFrame.

        Args:
            data_list (List[Any]): A list of pandas DataFrame objects.

        Returns:
            Any: A single pandas DataFrame resulting from concatenation.
        """
        if not data_list:
            raise ValueError("No data provided for merging.")
        return pd.concat(data_list, ignore_index=True)
