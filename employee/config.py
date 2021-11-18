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

# Logger Name
LOGGER_NAME = 'users'
LOGGER_LEVEL = logging.INFO
LOGGER_DSN = os.environ.get('LOGGER_DSN') or None

# Health check
HEALTH_CHECK = '/hello/'
APP_URL = os.environ.get('APP_URL', 'http://localhost:5000')

# art_relations database credentials.
AR_DB_CREDENTIALS = {
    'database': os.environ.get('AR_MYSQL_DATABASE'),
    'host': os.environ.get('AR_MYSQL_HOST'),
    'password': os.environ.get('AR_MYSQL_PASSWORD'),
    'port': os.environ.get('AR_MYSQL_PORT'),
    'user': os.environ.get('AR_MYSQL_USER')
}

# Database connection configuration.
QA_ENVIRONMENT = 'qa'
DEV_ENVIRONMENT = 'dev'
PROD_ENVIRONMENT = 'prod'
TEST_ENVIRONMENT = 'test'
ENVIRONMENT = os.environ.get('Environment') or DEV_ENVIRONMENT
ENVIRONMENTS = [
    QA_ENVIRONMENT, DEV_ENVIRONMENT, PROD_ENVIRONMENT, TEST_ENVIRONMENT]
if ENVIRONMENT == TEST_ENVIRONMENT:
    AR_DB_URL = 'sqlite://'
    POOL_CLASS = StaticPool
    CONNECT_ARGS = {'check_same_thread': False}
else:  # pragma: no cover
    # We must explicitly set utf8 encoding for MySQL connections.
    AR_DB_URL = (
        'mysql+pymysql://{sql6447613}:{AUyb61gwHi}@{freemysqlhosting.net}/{sql6447613}?charset={charset}'
        .format(
            user=AR_DB_CREDENTIALS.get('user'),
            password=AR_DB_CREDENTIALS.get('password'),
            host=AR_DB_CREDENTIALS.get('host'),
            db=AR_DB_CREDENTIALS.get('database'),
            charset='utf8'))
    POOL_CLASS = QueuePool
    POOL_SIZE = 15
    POOL_RECYCLE_MS = 3600  # Avoids connections going stale
    POOL_MAX_OVERFLOW = -1
    CONNECT_ARGS = {}
