"""Application configuration."""

import logging
import os
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir
from dotenv import load_dotenv
from sqlalchemy.pool import QueuePool
from sqlalchemy.pool import StaticPool


# Load environment variables from a .env file if present
dotenv_path = abspath(join(dirname(__file__), pardir, '.env'))
load_dotenv(dotenv_path)


# Service information
SERVICE_NAME = 'employee'
SERVICE_VERSION = '1.0.0'
os.environ['SERVICE_NAME'] = SERVICE_NAME

# Health check
HEALTH_CHECK = '/hello/'


# Database connection configuration.
DEV_ENVIRONMENT = 'dev'
TEST_ENVIRONMENT = 'test'
ENVIRONMENT = os.environ.get('Environment') or DEV_ENVIRONMENT
ENVIRONMENTS = [
    DEV_ENVIRONMENT, TEST_ENVIRONMENT]
if ENVIRONMENT == TEST_ENVIRONMENT:
    AR_DB_URL = 'sqlite://'
    POOL_CLASS = StaticPool
    CONNECT_ARGS = {'check_same_thread': False}
else:  # pragma: no cover
    # We must explicitly set utf8 encoding for MySQL connections.
    AR_DB_URL = (
        'mysql+pymysql://{user}:{password}@{host}/{db}'
        .format(
            user='sql6447613',
            password='AUyb61gwHi',
            host='sql6.freemysqlhosting.net',
            db='sql6447613'))
    '''POOL_CLASS = QueuePool
    POOL_SIZE = 15
    POOL_RECYCLE_MS = 3600  # Avoids connections going stale
    POOL_MAX_OVERFLOW = -1
    CONNECT_ARGS = {}
'''