import pytest
from unittest.mock import MagicMock

from app.db_connections.application.services import DatabaseConnectionService


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


def test_get_connector_valid(service, dummy_connector):
    """Verify that a valid connector is retrieved."""
    connector = service.get_connector("postgres")
    assert connector is dummy_connector


def test_get_connector_invalid(service):
    """Verify that retrieving an invalid connector raises ValueError."""
    with pytest.raises(ValueError):
        service.get_connector("unknown")


def test_open_connection(service, dummy_connector):
    """Verify that open_connection returns the dummy session."""
    result = service.open_connection()
    dummy_connector.connect.assert_called_once()
    assert result == "dummy_session"


def test_close_connection(service, dummy_connector):
    """Verify that close_connection calls the connector's disconnect method."""
    service.close_connection()
    dummy_connector.disconnect.assert_called_once()


def test_save_instance(service, dummy_connector):
    """Verify that save_instance calls the connector's save with the given instance."""
    dummy_instance = "instance"
    service.save_instance(dummy_instance)
    dummy_connector.save.assert_called_once_with(dummy_instance)


def test_update_instance(service, dummy_connector):
    """Verify that update_instance calls the connector's update with the given instance."""
    dummy_instance = "instance"
    service.update_instance(dummy_instance)
    dummy_connector.update.assert_called_once_with(dummy_instance)


def test_delete_instance(service, dummy_connector):
    """Verify that delete_instance calls the connector's delete with the given instance."""
    dummy_instance = "instance"
    service.delete_instance(dummy_instance)
    dummy_connector.delete.assert_called_once_with(dummy_instance)


def test_get_instance(service, dummy_connector):
    """Verify that get_instance returns the dummy instance."""
    model = "model"
    identifier = "id123"
    result = service.get_instance(model, identifier)
    dummy_connector.get.assert_called_once_with(model, identifier)
    assert result == "dummy_instance"


def test_get_all_instances(service, dummy_connector):
    """Verify that get_all_instances returns the list of dummy instances."""
    model = "model"
    result = service.get_all_instances(model)
    dummy_connector.get_all.assert_called_once_with(model)
    assert result == ["dummy_instance1", "dummy_instance2"]
