from typing import Any, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.db_connections.domain.ports import DBConnector
from app.db_connections.domain.models import ConnectionConfig


class PostgresConnector(DBConnector):
    """
    Concrete implementation of the DBConnector interface for PostgreSQL using SQLAlchemy ORM.

    This adapter uses a ConnectionConfig to build the SQLAlchemy engine and session.
    All CRUD operations and connection management are performed using the ORM.
    """

    def __init__(self, config: ConnectionConfig) -> None:
        """
        Initializes the PostgresConnector with the given connection configuration.

        Args:
            config (ConnectionConfig): The configuration details required to connect to PostgreSQL.
        """
        self.config = config
        self.engine = create_engine(
            f"postgresql+psycopg2://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}",
            echo=False,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.session: Session = None

    def connect(self) -> Session:
        """
        Establishes a connection to the PostgreSQL database and returns a SQLAlchemy session.

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
        Saves an ORM instance to the database.

        Args:
            instance (Any): The ORM object to be saved.
        """
        if not self.session:
            self.connect()
        self.session.add(instance)
        self.session.commit()

    def update(self, instance: Any) -> None:
        """
        Updates an existing ORM instance in the database.

        Args:
            instance (Any): The ORM object to be updated.
        """
        if not self.session:
            self.connect()
        self.session.merge(instance)
        self.session.commit()

    def delete(self, instance: Any) -> None:
        """
        Deletes an ORM instance from the database.

        Args:
            instance (Any): The ORM object to be deleted.
        """
        if not self.session:
            self.connect()
        self.session.delete(instance)
        self.session.commit()

    def get(self, model: Any, identifier: Any) -> Any:
        """
        Retrieves an instance of the specified model by its identifier.

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
        Retrieves all instances of the specified model.

        Args:
            model (Any): The ORM model class.

        Returns:
            List[Any]: A list of all instances of the model.
        """
        if not self.session:
            self.connect()
        return self.session.query(model).all()
