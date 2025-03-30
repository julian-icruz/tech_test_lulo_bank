from abc import ABC, abstractmethod
from typing import Any, List
from sqlalchemy.orm import Session


class DBConnector(ABC):
    """
    Interface for database connectors. Defines methods for managing database connections and interacting with the ORM.
    """

    @abstractmethod
    def connect(self) -> Session:
        """
        Establishes a connection to the database and returns the session.

        Returns:
            Session: A SQLAlchemy session used for querying and manipulating the database.
        """
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """
        Closes the connection to the database.
        """
        pass

    @abstractmethod
    def save(self, instance: Any) -> None:
        """
        Saves an instance to the database.

        Args:
            instance (Any): The ORM object to be saved (e.g., a model instance).
        """
        pass

    @abstractmethod
    def update(self, instance: Any) -> None:
        """
        Updates an existing instance in the database.

        Args:
            instance (Any): The ORM object to be updated.
        """
        pass

    @abstractmethod
    def delete(self, instance: Any) -> None:
        """
        Deletes an instance from the database.

        Args:
            instance (Any): The ORM object to be deleted.
        """
        pass

    @abstractmethod
    def get(self, model: Any, identifier: Any) -> Any:
        """
        Retrieves an instance by its identifier.

        Args:
            model (Any): The ORM model class.
            identifier (Any): The identifier of the instance to retrieve.

        Returns:
            Any: The retrieved ORM object or None if not found.
        """
        pass

    @abstractmethod
    def get_all(self, model: Any) -> List[Any]:
        """
        Retrieves all instances of a model from the database.

        Args:
            model (Any): The ORM model class.

        Returns:
            List[Any]: A list of all instances of the model.
        """
        pass
