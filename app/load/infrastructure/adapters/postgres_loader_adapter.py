from dataclasses import dataclass

from app.load.domain.ports import DataLoaderPort
from app.db_connections.application.services import DatabaseConnectionService


@dataclass
class PostgresLoaderAdapter(DataLoaderPort):
    """
    Adapter for loading data into PostgreSQL using the database connection service.

    Attributes:
        db_service (DatabaseConnectionService): Service to manage database connections.
    """

    db_service: dict[str, DatabaseConnectionService]

    def load_data(self, data: list[dict], model_class) -> None:
        """
        Inserts the received records into the database.

        Args:
            data (list[dict]): List of dictionaries containing the data to be inserted.
            model_class: ORM model class representing the target table.
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
