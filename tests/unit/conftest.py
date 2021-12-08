"""Test Configuration."""
from unittest.mock import MagicMock

import pytest

from employee import app


@pytest.fixture
def context():
    """Return flask app context, including a mock logger."""
    import application

    class MockLog:
        """Mock Logging Class."""

        def error(self):
            pass

        def info(self):
            pass

        def warning(self):
            pass

    context_instance = application.app.app_context()

    return context_instance


@pytest.fixture
def client():
    """Create an api test client."""
    return app.app.test_client()


@pytest.fixture
def app_ctx(app):
    """Create app context."""
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def req_ctx(app):
    """Create test request context."""
    with app.test_request_context() as ctx:
        yield ctx


def get_session_mock(return_data=[]):
    """GET get a mock for db_session() which returns return_data list."""
    enter_mock = MagicMock()
    session_mock = MagicMock()
    result_mock = MagicMock()
    session_mock.__enter__.return_value = enter_mock
    result_mock.single.return_value = return_data and return_data[0] or None
    result_mock.__iter__.return_value = return_data
    enter_mock.run.return_value = result_mock
    return session_mock


def get_transactional_session_mock(side_effect=[]):
    """Mock for session.read_transaction()."""
    enter_mock = MagicMock()
    result_mock = MagicMock()

    result_mock.data.side_effect = side_effect
    result_mock.single.side_effect = side_effect

    transaction_mock = MagicMock()
    transaction_mock.run.return_value = result_mock
    enter_mock.begin_transaction.return_value = transaction_mock

    session_mock = MagicMock()
    session_mock.__enter__.return_value = enter_mock
    return session_mock
