from typing import Any, Optional
from dataclasses import dataclass, field

from app.db_connections.domain.ports.db_connector import DBConnector


@dataclass
class DatabaseConnectionService:
    """
    Service layer that orchestrates database operations using a dictionary of DBConnector instances.

    This service provides a unified interface for performing CRUD operations and managing
    database connections for different databases by selecting the appropriate connector.
    The default connector is used unless explicitly changed.
    """

    connectors: dict[str, DBConnector]
    default_db_type: str = "postgres"
    connector: DBConnector = field(init=False)

    def __post_init__(self) -> None:

        self.connector = self.get_connector(self.default_db_type)

    def get_connector(self, db_type: Optional[str] = None) -> DBConnector:
        """
        Retrieves the connector for the specified database type.
        If db_type is None, returns the default connector.

        Args:
            db_type (Optional[str]): The key for the desired connector (e.g., "postgres" or "mysql").

        Returns:
            DBConnector: The corresponding connector.

        Raises:
            ValueError: If no connector exists for the given db_type.
        """
        if db_type is None:
            db_type = self.default_db_type
        connector = self.connectors.get(db_type)
        if connector is None:
            raise ValueError(f"Connector for '{db_type}' not found")
        return connector

    def select_connector(self, db_type: str) -> None:
        """
        Updates the current default connector to the one corresponding to the specified db_type.

        Args:
            db_type (str): The key for the desired connector.
        """
        self.connector = self.get_connector(db_type)

    def open_connection(self) -> Any:
        """
        Opens a connection to the database using the current default connector.

        Returns:
            Any: A database session object.
        """
        return self.connector.connect()

    def close_connection(self) -> None:
        """
        Closes the active database connection using the current default connector.
        """
        self.connector.disconnect()

    def save_instance(self, instance: Any) -> None:
        """
        Saves an ORM instance to the database using the current default connector.

        Args:
            instance (Any): The instance to be saved.
        """
        self.connector.save(instance)

    def update_instance(self, instance: Any) -> None:
        """
        Updates an ORM instance in the database using the current default connector.

        Args:
            instance (Any): The instance to be updated.
        """
        self.connector.update(instance)

    def delete_instance(self, instance: Any) -> None:
        """
        Deletes an ORM instance from the database using the current default connector.

        Args:
            instance (Any): The instance to be deleted.
        """
        self.connector.delete(instance)

    def get_instance(self, model: Any, identifier: Any) -> Any:
        """
        Retrieves an instance of a model from the database by its identifier using the current default connector.

        Args:
            model (Any): The ORM model class.
            identifier (Any): The unique identifier of the instance.

        Returns:
            Any: The retrieved ORM instance or None if not found.
        """
        return self.connector.get(model, identifier)

    def get_all_instances(self, model: Any) -> list[Any]:
        """
        Retrieves all instances of a model from the database using the current default connector.

        Args:
            model (Any): The ORM model class.

        Returns:
            List[Any]: A list of all ORM instances of the model.
        """
        return self.connector.get_all(model)
