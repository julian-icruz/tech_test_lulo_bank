from abc import ABC, abstractmethod


class DataLoaderPort(ABC):
    @abstractmethod
    def load_data(self, data: list[dict]) -> None:
        """
        Carga los datos en la base de datos.

        Args:
            data (list[dict]): Lista de registros (diccionarios) a insertar.
        """
        pass
