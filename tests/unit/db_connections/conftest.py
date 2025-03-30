import pytest
from unittest.mock import MagicMock, patch

from app.db_connections.domain.models import ConnectionConfig
from app.db_connections.application.services import DatabaseConnectionService


@pytest.fixture
def dummy_config_factory():
    def create_config(db_type="postgres", port=None, **kwargs):
        if port is None:
            port = 5432 if db_type == "postgres" else 3306
        return ConnectionConfig(
            db_type=db_type,
            host=kwargs.get("host", "localhost"),
            port=port,
            username=kwargs.get("username", "user"),
            password=kwargs.get("password", "pass"),
            database=kwargs.get("database", "test_db"),
            options=kwargs.get("options", {}),
        )

    return create_config


@pytest.fixture
def dummy_session():
    return MagicMock(name="dummy_session")


@pytest.fixture
def dummy_db_context():
    """
    Common fixture that patches SQLAlchemy's create_engine and sessionmaker for both
    PostgresConnector and MySQLConnector, returning a dummy session.
    """
    with (
        patch(
            "app.db_connections.infrastructure.adapters.relational.postgres_connector.create_engine"
        ) as mock_create_engine_pg,
        patch(
            "app.db_connections.infrastructure.adapters.relational.mysql_connector.create_engine"
        ) as mock_create_engine_mysql,
        patch(
            "app.db_connections.infrastructure.adapters.relational.postgres_connector.sessionmaker"
        ) as mock_sessionmaker_pg,
        patch(
            "app.db_connections.infrastructure.adapters.relational.mysql_connector.sessionmaker"
        ) as mock_sessionmaker_mysql,
    ):

        dummy_engine = MagicMock(name="dummy_engine")
        dummy_session = MagicMock(name="dummy_session")

        mock_create_engine_pg.return_value = dummy_engine
        mock_create_engine_mysql.return_value = dummy_engine
        mock_sessionmaker_pg.return_value = lambda: dummy_session
        mock_sessionmaker_mysql.return_value = lambda: dummy_session

        yield dummy_session


@pytest.fixture
def dummy_connector():
    """
    Returns a dummy connector mock with preset return values for its methods.
    """
    connector = MagicMock()
    connector.connect.return_value = "dummy_session"
    connector.disconnect.return_value = None
    connector.save.return_value = None
    connector.update.return_value = None
    connector.delete.return_value = None
    connector.get.return_value = "dummy_instance"
    connector.get_all.return_value = ["dummy_instance1", "dummy_instance2"]
    return connector


@pytest.fixture
def service(dummy_connector):
    """
    Creates a DatabaseConnectionService instance using a dictionary of connectors.
    """
    connectors = {"postgres": dummy_connector, "mysql": dummy_connector}
    return DatabaseConnectionService(connectors=connectors)
