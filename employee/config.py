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

from employee import constants


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

# exclude urls
USER_PROFILES_FOR_APP_URL = '/users/identity/<str>/application/<str>/profiles'
USER_IDENTITY_FROM_PROFILE_URL = '/profile/profile_id/<int>/profile_type/<str>/identity'

# List of all our existing environments:
#
# - test: the test environment is used by py.test to perform small adjustments
#   to the code. For instance: create the tables etc.
#
# - dev: the dev environment is used for development purposes. It points to
#   a different set of databases.
#
# - prod: production environment. Points directly to all our production
#   servers.
QA_ENVIRONMENT = 'qa'
DEV_ENVIRONMENT = 'dev'
PROD_ENVIRONMENT = 'prod'
TEST_ENVIRONMENT = 'test'

# Default email address to use as a sender.
SENDER_DEFAULT_EMAIL_ADDRESS = os.environ.get(
    'SENDER_DEFAULT_EMAIL_ADDRESS', 'donotreply@theorchard.com')

ENVIRONMENT = os.environ.get('Environment') or DEV_ENVIRONMENT
ENVIRONMENTS = [
    QA_ENVIRONMENT, DEV_ENVIRONMENT, PROD_ENVIRONMENT, TEST_ENVIRONMENT]
if ENVIRONMENT not in ENVIRONMENTS:
    raise Exception('The environment used is not properly named.')

APP_URL = os.environ.get('APP_URL', 'http://localhost:5000')

# Sentry configuration
SENTRY = os.environ.get('SENTRY_DSN') or None

# Dynamodb configuration
AWS_REGION = os.environ.get('AWS_REGION') or 'us-east-1'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
DYNAMODB_HOST = 'https://dynamodb.{}.amazonaws.com'.format(AWS_REGION)
DYNAMODB_SOCIAL_AUTH_TABLE = os.environ.get('DYNAMODB_SOCIAL_AUTH_TABLE')

# RSA information
RSA_LENGTH = 512
RSA_EXPIRATION = 3600 * 1000  # makes it valid for an hour, in ms

# Workstation URL
URL_WORKSTATION = ''.join([os.environ.get(
    'URL_WORKSTATION', 'http://workstation.qaorch.com'),
    '{resource}'])
# OA URL
URL_OA = ''.join([os.environ.get(
    'URL_OA', 'https://oa.qaorch.com'),
    '{resource}'])

# Workstation Secret
SECRET_WORKSTATION = os.environ.get(
    'SECRET_WORKSTATION',
    'dlAS*zH()1Y$7K5w3YR1/iz1Hvxz3E_l*B~x%cwodKkN85r?&yE^CO_d56<o8wY')
# OA Secret
SECRET_OA = os.environ.get(
    'SECRET_OA',
    'dlAS*zH()1Y$7K5w3YR1/iz1Hvxz3E_l*B~x%cwodKkN85r?&yE^CO_d56<o8wY')

# Public Key
# Note: the environment variables are not able to recognize the \n, so it
# doubles escape it (which leads to python not being able to understand it as
# it should). Replacing the \\n with \n works automatically.
UNIT_TEST_PRIVATE_KEY = (
    '-----BEGIN RSA PUBLIC KEY-----\nMEgCQQCGBCSqGeBOWXXGgqu6jWY5Mae73LgmB7H+r'
    'Qi/vZF8VQLWOrTvo7I3qMLL\n2ZoPYiKb/WMztIVxYsRsq+dZwpZlAgMBAAE=\n-----END '
    'RSA PUBLIC KEY-----\n')

PUBKEY_WORKSTATION = os.environ.get(
    'PUBKEY_WORKSTATION', UNIT_TEST_PRIVATE_KEY).replace('\\n', '\n')
PUBKEY_OA = os.environ.get(
    'PUBKEY_OA', UNIT_TEST_PRIVATE_KEY).replace('\\n', '\n')

# art_relations database credentials.
AR_DB_CREDENTIALS = {
    'database': os.environ.get('AR_MYSQL_DATABASE'),
    'host': os.environ.get('AR_MYSQL_HOST'),
    'password': os.environ.get('AR_MYSQL_PASSWORD'),
    'port': os.environ.get('AR_MYSQL_PORT'),
    'user': os.environ.get('AR_MYSQL_USER')
}

# Database connection configuration.
if ENVIRONMENT == TEST_ENVIRONMENT:
    AR_DB_URL = 'sqlite://'
    POOL_CLASS = StaticPool
    CONNECT_ARGS = {'check_same_thread': False}
else:  # pragma: no cover
    # We must explicitly set utf8 encoding for MySQL connections.
    AR_DB_URL = (
        'mysql+pymysql://{user}:{password}@{host}/{db}?charset={charset}'
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

# User information configuration.
USER_INFO_USER_TYPES = (
    constants.USER_INFO_USER_TYPE_OA,
    constants.USER_INFO_USER_TYPE_ALW
)

# AWS Secret key configuration
AWS_SECRET_MANAGER_URL = 'https://secretsmanager.us-east-1.amazonaws.com'
FEATURE_FM_SECRET_TOKEN = os.environ.get('FEATURE_FM_SECRET_TOKEN') or None
FEATURE_FM_SECRET_TOKEN_KEY = os.environ.get(
    'FEATURE_FM_SECRET_TOKEN_KEY') or None

AUTH0_MACHINE_CLIENT_ID = os.environ.get('AUTH0_MACHINE_CLIENT_ID')
AUTH0_MACHINE_CLIENT_SECRET = os.environ.get('AUTH0_MACHINE_CLIENT_SECRET')
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', 'orch-labs.auth0.com')
AUTH0_URL = 'https://{}/api/v2/'.format(AUTH0_DOMAIN)
AUTH0_CONNECTION = os.environ.get('AUTH0_CONNECTION', 'art-relations')
AUTH0_INSIGHTS_APP_NAME = 'insights-login'
AUTH0_ORG_INVITE_TTL = 172800  # 48 hrs


DAEMON_NOTIFICATIONS_SQS_URL = os.environ.get(
    'DAEMON_NOTIFICATIONS_SQS_URL',
    'https://sqs.us-east-1.amazonaws.com/103233932089/dev-ows-notification')

LRU_CACHE_CURRENCY_CODES = os.environ.get('LRU_CACHE_CURRENCY_CODES') or 1000

NEO4J_MAX_RETRY_TIME = os.environ.get('NEO4J_MAX_RETRY_TIME') or 30  # 30s
# Neo4j Aura

FCM_APPLICATION_ARN = os.environ.get('FCM_APPLICATION_ARN') or None
APN_APPLICATION_ARN = os.environ.get('APN_APPLICATION_ARN') or None
AWAL_FCM_APPLICATION_ARN = os.environ.get('AWAL_FCM_APPLICATION_ARN') or None
AWAL_APN_APPLICATION_ARN = os.environ.get('AWAL_APN_APPLICATION_ARN') or None
PUSH_NOTIFICATION_ARN = {
    f'ios_{constants.ORCHARD_BRAND}': APN_APPLICATION_ARN,
    f'android_{constants.ORCHARD_BRAND}': FCM_APPLICATION_ARN,
    f'ios_{constants.AWAL_BRAND}': AWAL_APN_APPLICATION_ARN,
    f'android_{constants.AWAL_BRAND}': AWAL_FCM_APPLICATION_ARN,
}


SNS_ARN_PREFIX = os.environ.get(
    'SNS_ARN_PREFIX',
    'arn:aws:sns:us-east-1:103233932089')
DELIVERY_STATUS_LOGGING_ROLE = os.environ.get(
    'DELIVERY_STATUS_LOGGING_ROLE', '')

# Redis Caching
REDIS_URL = os.environ.get('REDIS_URL', None)
REDIS_CACHE_TTL = os.environ.get('REDIS_CACHE_TTL', 86400)  # 24 hrs

ORCHARD_DOMAIN = (
    'theorchard.com' if ENVIRONMENT == PROD_ENVIRONMENT else 'qaorch.com')
AWAL_DOMAIN = (
    'awal.com' if ENVIRONMENT == PROD_ENVIRONMENT else 'qaawal.com')

SONGWHIP_DOMAIN = (
    'songwhip.com' if ENVIRONMENT == PROD_ENVIRONMENT
    else 'staging.songwhip.com')

PROFILE_TYPE_APPLICATION_MAPPING = {
    constants.LABEL_PROFILE: {
        'name': 'Workstation',
        'id': 'workstation',
        'url': 'https://workstation.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.PODCAST_PROFILE: {
        'name': 'Podcasts',
        'id': 'podcasts',
        'url': 'https://podcast.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.PUBLISHING_PROFILE: {
        'name': 'Publishing',
        'id': 'publishing',
        'url': 'https://publishing.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.INSIGHTS_PROFILE: {
        'name': 'Insights',
        'id': 'insights',
        'url': 'https://insights.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.ORCHADMIN_PROFILE: {
        'name': 'Orchadmin',
        'id': 'orchadmin',
        'url': 'https://oa.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.ABACUS_PROFILE: {
        'name': 'Abacus',
        'id': 'abacus',
        'url': 'https://abacus.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.MONEYHUB_PROFILE: {
        'name': 'MoneyHub',
        'id': 'moneyhub',
        'url': 'https://moneyhub.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.SETTINGS_PROFILE: {
        'name': 'Settings',
        'id': 'settings',
        'url': 'https://settings.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.CONTENT_PROFILE: {
        'name': 'Content',
        'id': 'content',
        'url': 'https://content.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.COLLABORATORS_PROFILE: {
        'name': 'Collaborators',
        'id': 'collaborators',
        'url': 'https://collaborators.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.SONGWHIP_PROFILE: {
        'name': 'Songwhip',
        'id': 'songwhip',
        'url': 'https://{0}'.format(SONGWHIP_DOMAIN)
    },
    constants.NR_PROFILE: {
        'name': 'NR',
        'id': 'nr',
        'url': 'https://nr.{0}'.format(ORCHARD_DOMAIN)
    },
    constants.DOCUMENTS_PROFILE: {
        'name': 'NR',
        'id': 'nr',
        'url': 'https://documents.{0}'.format(ORCHARD_DOMAIN)
    }
}

ONLY_LOG_ACCESS_ERRORS = True if ENVIRONMENT == PROD_ENVIRONMENT else False
