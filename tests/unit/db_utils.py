from contextlib import contextmanager
from functools import wraps
import sys
from unittest import mock

from employee import config
from employee.connectors import mysql
from employee.connectors.mysql import db_session


def seed_models(models):
   # import pdb; pdb.set_trace()
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
    mock_session = mock.Mock(query=mock.Mock())

    @contextmanager
    def fake_session_manager():
        yield mock_session

    mocker.patch.object(mysql, 'db_session', fake_session_manager)

    return mock_session