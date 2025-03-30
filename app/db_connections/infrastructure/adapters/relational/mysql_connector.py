from typing import Any, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.db_connections.domain.ports import DBConnector
from app.db_connections.domain.models import ConnectionConfig


class MySQLConnector(DBConnector):
    """
    Concrete implementation of the DBConnector interface for MySQL using SQLAlchemy ORM.

    This adapter leverages a ConnectionConfig to establish a connection to a MySQL database.
    All CRUD operations and connection management are performed using the ORM.
    """

    def __init__(self, config: ConnectionConfig) -> None:
        """
        Initializes the MySQLConnector with the provided connection configuration.

        Args:
            config (ConnectionConfig): The configuration details required to connect to MySQL.
        """
        self.config = config
        self.engine = create_engine(
            f"mysql+mysqlconnector://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}",
            echo=False,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.session: Session = None

    def connect(self) -> Session:
        """
        Establishes a connection to the MySQL database and returns a SQLAlchemy session.

        Returns:
            Session: A SQLAlchemy session for database operations.
        """
        self.session = self.SessionLocal()
        return self.session

    def disconnect(self) -> None:
        """
        Closes the active database session.
        """
        if self.session:
            self.session.close()
            self.session = None

    def save(self, instance: Any) -> None:
        """
        Saves an ORM instance to the MySQL database.

        Args:
            instance (Any): The ORM object to be saved.
        """
        if not self.session:
            self.connect()
        self.session.add(instance)
        self.session.commit()

    def update(self, instance: Any) -> None:
        """
        Updates an existing ORM instance in the MySQL database.

        Args:
            instance (Any): The ORM object to be updated.
        """
        if not self.session:
            self.connect()
        self.session.merge(instance)
        self.session.commit()

    def delete(self, instance: Any) -> None:
        """
        Deletes an ORM instance from the MySQL database.

        Args:
            instance (Any): The ORM object to be deleted.
        """
        if not self.session:
            self.connect()
        self.session.delete(instance)
        self.session.commit()

    def get(self, model: Any, identifier: Any) -> Any:
        """
        Retrieves an instance of the specified model by its identifier from the MySQL database.

        Args:
            model (Any): The ORM model class.
            identifier (Any): The unique identifier of the instance.

        Returns:
            Any: The retrieved ORM object or None if not found.
        """
        if not self.session:
            self.connect()
        return self.session.get(model, identifier)

    def get_all(self, model: Any) -> List[Any]:
        """
        Retrieves all instances of the specified model from the MySQL database.

        Args:
            model (Any): The ORM model class.

        Returns:
            List[Any]: A list of all instances of the model.
        """
        if not self.session:
            self.connect()
        return self.session.query(model).all()
