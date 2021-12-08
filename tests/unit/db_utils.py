"""Utilities for working with DB in tests."""
from contextlib import contextmanager
from functools import wraps
import sys
from unittest import mock

from employee import config
from employee.connectors import mysql


def seed_models(models):
    """Save the given model(s) to the DB.

    Args:
        models (list): list of model instances to save.
    """
    if not hasattr(models, '__iter__'):
        models = [models]

    with mysql.db_session() as session:
        _exit_if_not_test_environment(session)
        for model in models:
            session.add(model)
        session.flush()

        # detach the objects from this session so tests can interrogate them
        for model in models:
            session.expunge(model)


def test_schema(function):
    """Test schema.

    Decorator that creates the test DB schema before a function call and
    tears the schema down after the function call has finished.

    This just creates the schema and does not seed data. Indvidual test cases
    can use factories to seed data as needed.

    Args:
        Function (func): function to be called after creating the test schema.

    Returns:
        Function: The decorated function.

    """
    @wraps(function)
    def call_function_within_db_context(*args, **kwargs):
        with mysql.db_session() as session:
            _exit_if_not_test_environment(session)
        mysql.BaseModel.metadata.create_all(mysql.db_engine)
        try:
            function_return = function(*args, **kwargs)
        finally:
            mysql.BaseModel.metadata.drop_all(mysql.db_engine)

        return function_return
    return call_function_within_db_context


def _exit_if_not_test_environment(session):
    if config.ENVIRONMENT != config.TEST_ENVIRONMENT:
        sys.exit('Environment must be set to {}.'.format(
            config.TEST_ENVIRONMENT))
    if 'sqlite' not in session.bind.url.drivername:
        sys.exit('Tests must point to sqlite database.')


def mock_db_session(mocker):
    """Create a mock database session.

    Also mock the db_session context manager to use the mock session.
    """
    mock_session = mock.Mock(query=mock.Mock())

    @contextmanager
    def fake_session_manager():
        yield mock_session

    mocker.patch.object(mysql, 'db_session', fake_session_manager)

    return mock_session
