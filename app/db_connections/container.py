from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dict, Factory, Singleton

from app.db_connections import Settings

from app.db_connections.domain.models import ConnectionConfig
from app.db_connections.infrastructure.adapters.relational import (
    PostgresConnector,
    MySQLConnector,
)

from app.db_connections.application.services import DatabaseConnectionService


class DBConnectionsContainer(DeclarativeContainer):
    """
    Dependency injection container for the db_connections bounded context.

    This container provides configuration and factories for the database connector adapters and the
    DatabaseConnectionService. It abstracts the creation of concrete connector instances (e.g., PostgreSQL or MySQL)
    using a ConnectionConfig, allowing easy substitution and extension.
    """

    settings = Settings()

    config_postgres = Factory(
        ConnectionConfig,
        db_type="postgres",
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        username=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DB,
        options={},
    )

    config_mysql = Factory(
        ConnectionConfig,
        db_type="mysql",
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        username=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DB,
        options={},
    )

    postgres_connector = Singleton(
        PostgresConnector,
        config=config_postgres,
    )

    mysql_connector = Singleton(
        MySQLConnector,
        config=config_mysql,
    )

    connectors = Dict(
        postgres=postgres_connector,
        mysql=mysql_connector,
    )

    database_connection_service = Singleton(
        DatabaseConnectionService, connectors=connectors
    )
