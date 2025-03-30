from pydantic import BaseModel
from typing import Optional


class ConnectionConfig(BaseModel):
    """
    Data Transfer Object (DTO) for database connection configuration.

    This model encapsulates the settings required to establish a connection to a database.

    Attributes:
        db_type (str): The type of the database (e.g., 'postgres', 'mysql', 'dynamodb', 'datastore').
        host (str): The hostname or IP address of the database server.
        port (int): The port number on which the database server is listening.
        username (Optional[str]): The username for authenticating with the database.
        password (Optional[str]): The password for authenticating with the database.
        database (Optional[str]): The name of the database to connect to.
        options (Optional[dict[str, str]]): Additional connection options if needed.
    """

    db_type: str
    host: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None
    database: Optional[str] = None
    options: Optional[dict[str, str]] = None
