from unittest.mock import MagicMock, patch

from app.db_connections import DBConnectionsContainer
from app.db_connections.domain.models import ConnectionConfig
from app.db_connections.infrastructure.adapters.relational import (
    PostgresConnector,
    MySQLConnector,
)

from app.db_connections.application.services import DatabaseConnectionService


@patch(
    "app.db_connections.infrastructure.adapters.relational.postgres_connector.create_engine",
    return_value=MagicMock(),
)
def test_postgres_connector_instance(mock_create_engine):
    container = DBConnectionsContainer()
    pg_connector = container.postgres_connector()
    assert isinstance(pg_connector, PostgresConnector)
    config: ConnectionConfig = pg_connector.config
    assert config.db_type == "postgres"
    assert config.host == DBConnectionsContainer.settings.POSTGRES_HOST


@patch(
    "app.db_connections.infrastructure.adapters.relational.mysql_connector.create_engine",
    return_value=MagicMock(),
)
def test_mysql_connector_instance(mock_create_engine):
    container = DBConnectionsContainer()
    mysql_connector = container.mysql_connector()
    assert isinstance(mysql_connector, MySQLConnector)
    config: ConnectionConfig = mysql_connector.config
    assert config.db_type == "mysql"
    assert config.host == DBConnectionsContainer.settings.MYSQL_HOST


def test_connectors_dict():
    with (
        patch(
            "app.db_connections.infrastructure.adapters.relational.postgres_connector.create_engine",
            return_value=MagicMock(),
        ),
        patch(
            "app.db_connections.infrastructure.adapters.relational.mysql_connector.create_engine",
            return_value=MagicMock(),
        ),
    ):
        container = DBConnectionsContainer()
        connectors = container.connectors()
        assert "postgres" in connectors
        assert "mysql" in connectors
        assert isinstance(connectors["postgres"], PostgresConnector)
        assert isinstance(connectors["mysql"], MySQLConnector)


def test_database_connection_service_singleton():
    with (
        patch(
            "app.db_connections.infrastructure.adapters.relational.postgres_connector.create_engine",
            return_value=MagicMock(),
        ),
        patch(
            "app.db_connections.infrastructure.adapters.relational.mysql_connector.create_engine",
            return_value=MagicMock(),
        ),
    ):
        container = DBConnectionsContainer()
        service1 = container.database_connection_service()
        service2 = container.database_connection_service()
        assert service1 is service2
        assert isinstance(service1, DatabaseConnectionService)
