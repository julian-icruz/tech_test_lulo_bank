from typing import Any, List
from dataclasses import dataclass
from app.db_connections.domain.ports import DBConnector


@dataclass
class DatabaseConnectionService:
    """
    Service layer that orchestrates database operations using a provided DBConnector.

    This service provides a unified interface for performing CRUD operations and managing
    database connections, abstracting the details of the underlying connector implementation.
    """

    connector: DBConnector

    def open_connection(self) -> Any:
        """
        Opens a connection to the database using the connector.

        Returns:
            Any: A database session object.
        """
        return self.connector.connect()

    def close_connection(self) -> None:
        """
        Closes the active database connection.
        """
        self.connector.disconnect()

    def save_instance(self, instance: Any) -> None:
        """
        Saves an ORM instance to the database.

        Args:
            instance (Any): The instance to be saved.
        """
        self.connector.save(instance)

    def update_instance(self, instance: Any) -> None:
        """
        Updates an ORM instance in the database.

        Args:
            instance (Any): The instance to be updated.
        """
        self.connector.update(instance)

    def delete_instance(self, instance: Any) -> None:
        """
        Deletes an ORM instance from the database.

        Args:
            instance (Any): The instance to be deleted.
        """
        self.connector.delete(instance)

    def get_instance(self, model: Any, identifier: Any) -> Any:
        """
        Retrieves an instance of a model from the database by its identifier.

        Args:
            model (Any): The ORM model class.
            identifier (Any): The unique identifier of the instance.

        Returns:
            Any: The retrieved ORM instance or None if not found.
        """
        return self.connector.get(model, identifier)

    def get_all_instances(self, model: Any) -> List[Any]:
        """
        Retrieves all instances of a model from the database.

        Args:
            model (Any): The ORM model class.

        Returns:
            List[Any]: A list of all ORM instances of the model.
        """
        return self.connector.get_all(model)
