"""MySQL Connector.

Manages interactions with MySQL.
"""

from contextlib import contextmanager
import functools

from flask import g, response
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
    session = _db_session()
    try:
        yield session
    except Exception:
        raise
    finally:
        session.close()
