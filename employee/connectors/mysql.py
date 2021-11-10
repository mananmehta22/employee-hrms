"""MySQL Connector.

Manages interactions with MySQL.
"""

from contextlib import contextmanager
import functools

from flask import g
from owsresponse import response
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from employee import config

# please don't use the following private variables directly;
# use db_session
if config.POOL_CLASS == QueuePool:
    db_engine = create_engine(
        config.AR_DB_URL, pool_size=config.POOL_SIZE,
        max_overflow=config.POOL_MAX_OVERFLOW,
        pool_recycle=config.POOL_RECYCLE_MS,
        connect_args=config.CONNECT_ARGS)
else:
    db_engine = create_engine(
        config.AR_DB_URL,
        connect_args=config.CONNECT_ARGS,
        poolclass=config.POOL_CLASS)
_db_session = sessionmaker(bind=db_engine)

BaseModel = declarative_base()


@contextmanager
def db_session():
    """Provide a transactional scope around a series of operations.

    Taken from http://docs.sqlalchemy.org/en/latest/orm/session_basics.html.
    This handles rollback and closing of session, so there is no need
    to do that throughout the code.

    Usage:
        with db_session() as session:
            session.execute(query)
    """
    session = _db_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def db_read_session():
    """Provide a read scope around a series of operations.

    This handles closing of session.
    No commit or rollback so use only for SELECT queries.

    Usage:
        with db_session() as session:
            session.execute(query)
    """
    session = _db_session()
    try:
        yield session
    except Exception:
        raise
    finally:
        session.close()


def wrap_db_errors(function):
    """Decorate the given function with logic to handle SQLAlchemy errors.

    If a SQLAlchemy exception is thrown, it will be caught and logged and the
    function will return a fatal response.

    Args:
        function (func): the function to decorate

    Returns:
        func: function decorated with error-handling logic

    """
    @functools.wraps(function)
    def call_function_with_error_handling(*args, **kwargs):
        try:
            function_return = function(*args, **kwargs)
        except exc.SQLAlchemyError as exception:
            sentry.sentry_client.captureMessage(exception, stack=True)
            g.ows.log.error('DB error: {}'.format(exception))
            return response.create_fatal_response()

        return function_return
    return call_function_with_error_handling
