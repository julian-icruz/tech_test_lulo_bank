import pytest

from app.db_connections.domain.models import ConnectionConfig


def test_connection_config_valid():
    config = ConnectionConfig(
        db_type="postgres",
        host="localhost",
        port=5432,
        username="admin",
        password="secret",
        database="test_db",
        options={"ssl": "true"},
    )
    assert config.db_type == "postgres"
    assert config.host == "localhost"
    assert config.port == 5432
    assert config.username == "admin"
    assert config.password == "secret"
    assert config.database == "test_db"
    assert config.options == {"ssl": "true"}


def test_connection_config_defaults():
    config = ConnectionConfig(db_type="mysql", host="mysql-server", port=3306)
    assert config.db_type == "mysql"
    assert config.host == "mysql-server"
    assert config.port == 3306
    assert config.username is None
    assert config.password is None
    assert config.database is None
    assert config.options is None


def test_connection_config_missing_required():
    with pytest.raises(Exception):
        ConnectionConfig(host="localhost", port=5432, username="admin")
