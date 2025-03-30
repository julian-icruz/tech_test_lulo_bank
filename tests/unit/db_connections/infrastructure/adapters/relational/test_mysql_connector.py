import pytest
from unittest.mock import MagicMock

from app.db_connections.infrastructure.adapters.relational import MySQLConnector

# )


@pytest.fixture
def connector(dummy_config_factory, dummy_db_context):
    config = dummy_config_factory(db_type="postmysqlgres", port=3306)
    conn = MySQLConnector(config)
    yield conn


def test_connect_returns_session(connector, dummy_db_context):
    session = connector.connect()
    assert session is dummy_db_context
    assert connector.session is dummy_db_context


def test_disconnect_sets_session_none(connector, dummy_session):
    connector.session = dummy_session
    connector.disconnect()
    assert connector.session is None


def test_save_calls_session_methods(connector, dummy_session):
    connector.session = dummy_session
    dummy_instance = MagicMock(name="dummy_instance")
    connector.save(dummy_instance)
    dummy_session.add.assert_called_once_with(dummy_instance)
    dummy_session.commit.assert_called_once()


def test_update_calls_session_methods(connector, dummy_session):
    connector.session = dummy_session
    dummy_instance = MagicMock(name="dummy_instance")
    connector.update(dummy_instance)
    dummy_session.merge.assert_called_once_with(dummy_instance)
    dummy_session.commit.assert_called_once()


def test_delete_calls_session_methods(connector, dummy_session):
    connector.session = dummy_session
    dummy_instance = MagicMock(name="dummy_instance")
    connector.delete(dummy_instance)
    dummy_session.delete.assert_called_once_with(dummy_instance)
    dummy_session.commit.assert_called_once()


def test_get_calls_session_get(connector, dummy_session):
    connector.session = dummy_session
    dummy_model = MagicMock(name="dummy_model")
    identifier = "id123"
    connector.get(dummy_model, identifier)
    dummy_session.get.assert_called_once_with(dummy_model, identifier)


def test_get_all_calls_query(connector, dummy_session):
    connector.session = dummy_session
    dummy_model = MagicMock(name="dummy_model")
    query_mock = MagicMock(name="query_mock")
    dummy_session.query.return_value = query_mock
    connector.get_all(dummy_model)
    dummy_session.query.assert_called_once_with(dummy_model)
    query_mock.all.assert_called_once()
