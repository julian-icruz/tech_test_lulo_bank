from app.load.domain.ports import DataLoaderPort
from app.db_connections.application.services import DatabaseConnectionService


class PostgresLoaderAdapter(DataLoaderPort):
    def __init__(self, db_connection_service: DatabaseConnectionService):
        self.db_service = db_connection_service

    def load_data(self, data: list[dict], model_class) -> None:
        """
        Inserta en la base de datos los registros recibidos.

        Args:
            data (list[dict]): Lista de diccionarios con los datos a insertar.
            model_class: Clase del modelo ORM que representa la tabla destino.
        """
        session = self.db_service.open_connection()
        try:
            for record in data:
                instance = model_class(**record)
                session.add(instance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            self.db_service.close_connection()
