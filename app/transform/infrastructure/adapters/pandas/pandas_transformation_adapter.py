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
        return data.drop(columns=["_embedded", "_links", "image"]).drop_duplicates()

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
        # Convertir listas a cadenas
        df_cleaned = df.applymap(lambda x: str(x) if isinstance(x, list) else x)

        # Eliminar filas duplicadas
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
