"""Constants for the application."""
import os

MULTIPLE_ACCOUNTS_SAME_EMAIL_ERROR_CODE = 'error_multiples_account_same_email'
MULTIPLE_ACCOUNTS_SAME_EMAIL_ERROR = (
    'More than one account is using this email address. Please use your login '
    'instead.')

LOGIN_ERROR_CODE = 'invalid_login'
LOGIN_ERROR = 'Incorrect login, please try again.'

TOKEN_EXPIRED_ERROR_CODE = 'expired_token'
TOKEN_EXPIRED_ERROR = 'The token has expired.'

TOKEN_REVOKED_ERROR_CODE = 'revoked_token'
TOKEN_REVOKED_ERROR = 'The token had been revoked.'

BAD_PARAMS_ERROR_CODE = 'bad_params'
BAD_PARAMS_ERROR_message = 'bad params'

ERROR_CODE_NOT_FOUND = 'not_found'
ERROR_CODE_VALIDATION_ERROR = 'validation_error'
ERROR_CODE_ALREADY_EXISTS = 'already_exists'
ERROR_CODE_AUTHORIZATION_ERROR = 'authorization_error'
ERROR_CODE_CREATE_ERROR = 'create_error'

ERROR_CODE_IDENTITY_NOT_FOUND = ERROR_CODE_NOT_FOUND
ERROR_MESSAGE_IDENTITY_NOT_FOUND = (
    'Identity not found')
ERROR_CODE_IDENTITY_ALREADY_EXISTS = ERROR_CODE_ALREADY_EXISTS
ERROR_MESSAGE_IDENTITY_ALREADY_EXISTS = (
    'Identity already exists.'
)
ERROR_MESSAGE_IDENTITY_ALREADY_EXISTS_EMAIL = (
    'Identity already exists with this email.'
)
ERROR_MESSAGE_PROFILE_NOT_FOUND = (
    'Profile not found')
ERROR_MESSAGE_PROFILE_EXISTS = (
    'Profile already exists')
ERROR_CODE_RELATIONSHIP_ALREADY_EXISTS = ERROR_CODE_ALREADY_EXISTS
ERROR_MESSAGE_RELATIONSHIP_ALREADY_EXISTS = (
    'Relationship already exists.'
)

ERROR_CODE_IDENTITY_VALIDATION_ERROR = ERROR_CODE_VALIDATION_ERROR
ERROR_CODE_PROFILE_VALIDATION_ERROR = ERROR_CODE_VALIDATION_ERROR
ERROR_MESSAGE_PROFILE_VALIDATION_ERROR = 'The profile is invalid.'

ERROR_CODE_VENDOR_AGREEMENT_NOT_FOUND = ERROR_CODE_NOT_FOUND
ERROR_MESSAGE_VENDOR_AGREEMENT_NOT_FOUND = 'Vendor agreement not found'

ERROR_INVALID_APP = 'INVALID_APP'
ERROR_NOT_IMPLEMENTED = 'NOT_IMPLEMENTED'

EXPIRED_LOGIN_TOKEN_ERROR_CODE = 'expired_login_token'
EXPIRED_LOGIN_TOKEN_ERROR = (
    'Your session has expired, please refresh the page and try again.')

MESSAGE_SES_AUTH_FAILED = 'SES Auth Failed: No Amazon Credentials Found'
MESSAGE_SES_DELIVERY_FAILED = 'Email Failed for %s: %s'
MESSAGE_SES_UNKNON_EXCEPTION = 'Unknown Email Exception %s for: %s'
EMAIL_TITLE_FORGOTTEN_PASSWORD = 'Forgotten password reset'

MESSAGE_UNSUCCESFUL_KEY_GENERATION = 'Generating the keys was not successful.'

ERROR_MISSING_REQUIRED_ID = 'Either user_id or auth0_id is required.'

ERROR_MESSAGE_DELETE_RELATIONSHIP_FAILED = \
    'Failed to delete relationship. Please check if relationship between ' \
    'both nodes exist.'
ERROR_MESSAGE_CREATE_RELATIONSHIP_FAILED = \
    'Failed to create relationship. Please check if both the nodes exist.'
WARNING_MESSAGE_EMPTY_RESPONSE = 'Endpoint {} returned an empty response.'

# User information constants.

# User types that user information endpoints work with.
USER_INFO_USER_TYPE_OA = 'oa'
USER_INFO_USER_TYPE_ALW = 'alw'


# API errors.
UNSUPPORTED_USER_TYPE_CODE = 'unsupported_user_type'
UNSUPPORTED_USER_TYPE = 'This user type is not supported.'

# Query parameters.
QUERY_PARAM_USER_TYPE = 'type'

GRASS_ACCOUNT_TYPE = 'Grass-Account-Type'
GRASS_ACCOUNT_ID = 'Grass-Account-Id'
GRASS_ACCOUNT_TYPE_VENDOR = 'vendor'
GRASS_ACCOUNT_TYPE_SUBACCOUNT = 'subaccount'

# User Context types
PROFILE_CONTEXT_TYPE = 'profile'

GRASS_ACCOUNT_TYPES = [
    GRASS_ACCOUNT_TYPE_VENDOR, GRASS_ACCOUNT_TYPE_SUBACCOUNT]

ORCHARD_USER_ID = 'Orchard-User-Id'

URL_PATHS = {
    'feature-fm': '/orchardlogin'
}

# Pagination
PAGINATION_TYPE_STANDARD = 'standard'

SSO_NOTIFICATION_FEED_NAME = 'single_signon'
SSO_NOTIFICATION_TEMPLATE = 'auth0_sso'

# feature flag names
FEATURE_DEACTIVATE_WORKSTATION_USER = 'deactivate_workstation_user'
FEATURE_WS_NEO4J_NUMBER_FORMAT = 'workstation_neo4j_number_format'
FEATURE_SHOW_MONEYHUB_APP = 'orchard_suite_show_moneyhub_app'
FEATURE_SHOW_COLLABORATORS_APP = 'collaborators_suite'
EDIT_SUPER_ADMINS = 'settings_app_edit_super_admins'
FEATURE_SHOW_NR_APP = 'neighbouring_rights_suite'

# Ows Account
CONTENT_TYPE = 'application/json'
OWS_ACCOUNT = 'ows-account'
ERROR_CODE_OWS_ACCOUNT_REQUEST = 'ows_account_error'

# Feature FM permissions
CAMPAIGNS_FEATURE_NAME = 'Orchard Advertising'
WHITELIST_FEATURE_NAME = 'Orchard Advertising Tier 1'
FACEBOOK_BOOST_NAME = 'Facebook Campaign Boost'
MARKETING_ROLE_ID = 2
ADVERTISING_ROLE_ID = 7
ADMIN_ROLE_ID = 4

# Preference constants
DEFAULT_CURRENCY_CODE = 'USD'
LOCALES = {
    'English': 'en',
    'German': 'de',
    'Spanish': 'es',
    'French': 'fr',
    'Italian': 'it',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Turkish': 'tr',
    'Chinese': 'zh-CN',
    'Chinese (TW)': 'zh-TW'
}
NUMBER_FORMAT = ['us', 'eu']
# Map Neo4j number_format to vend_contact number_format values.
NUMBER_FORMAT_MAPPING_TO_LEGACY = {
    'us': 'us',
    'eu': 'europe',
}

MISSING_STATUS_MESSAGE = 'Data should contain active field with value Y or N.'

"""Default pagination values in case user does not specify."""

PAGE_OFFSET_DEFAULT = 0  # start with first record
PAGE_LIMIT_DEFAULT = 50  # max number of records


# Constants for Mocking response for Demo purpose only.

MOCK_RESPONSE_FOLDER = os.path.dirname(os.path.realpath(
    __file__)) + '/mock_responses/'

ABACUS_PROFILE = 'AbacusProfile'
ARTIST_PROFILE = 'ArtistProfile'
COLLABORATORS_PROFILE = 'CollaboratorsProfile'
CONTENT_PROFILE = 'ContentProfile'
INSIGHTS_PROFILE = 'InsightsProfile'
LABEL_PROFILE = 'LabelProfile'
ORCHADMIN_PROFILE = 'OrchAdminProfile'
SETTINGS_PROFILE = 'SettingsProfile'
PODCAST_PROFILE = 'PodcastProfile'
PUBLISHING_PROFILE = 'PublishingProfile'
MONEYHUB_PROFILE = 'MoneyhubProfile'
SWITCHBOARD_PROFILE = 'SwitchboardProfile'
DISTRO_DEV_PROFILE = 'DistroDevProfile'
SONGWHIP_PROFILE = 'SongwhipProfile'
NR_PROFILE = 'NRProfile'
DOCUMENTS_PROFILE = 'DocumentsProfile'

PROFILE_TYPES = (ARTIST_PROFILE, LABEL_PROFILE, SWITCHBOARD_PROFILE,
                 PODCAST_PROFILE, PUBLISHING_PROFILE, INSIGHTS_PROFILE, ORCHADMIN_PROFILE,
                 DISTRO_DEV_PROFILE, ABACUS_PROFILE, MONEYHUB_PROFILE,
                 CONTENT_PROFILE, SONGWHIP_PROFILE, NR_PROFILE, DOCUMENTS_PROFILE)

APPLICATION_WORKSTATION = 'workstation'
APPLICATION_ORCHARDGO = 'orchard-go'
APPLICATION_SWITCHBOARD = 'switchboard'
APPLICATION_PODCAST = 'frontend-podcast'
APPLICATION_PUBLISHING = 'frontend-publishing'
APPLICATION_INSIGHTS = 'frontend-insights'
APPLICATION_ORCHADMIN = 'oa'
APPLICATION_DISTRO_SANDBOX = 'frontend-distro-sandbox'
APPLICATION_SETTINGS = 'frontend-settings'
APPLICATION_ABACUS = 'frontend-royalties'
APPLICATION_MONEYHUB = 'frontend-moneyhub'
APPLICATION_CONTENT = 'frontend-content-review'
APPLICATION_COLLABORATOR = 'frontend-collaborator-suite'
APPLICATION_SONGWHIP = 'songwhip'
APPLICATION_NR = 'frontend-neighbouring-rights'
APPLICATION_DOCUMENTS = 'frontend-documents'

APPLICATION_PROFILE_TYPE_MAPPING = {
    APPLICATION_ORCHARDGO: (INSIGHTS_PROFILE,),
    APPLICATION_WORKSTATION: (LABEL_PROFILE,),
    APPLICATION_SWITCHBOARD: (SWITCHBOARD_PROFILE,),
    APPLICATION_PODCAST: (PODCAST_PROFILE,),
    APPLICATION_PUBLISHING: (PUBLISHING_PROFILE,),
    APPLICATION_MONEYHUB: (MONEYHUB_PROFILE,),
    APPLICATION_INSIGHTS: (INSIGHTS_PROFILE,),
    APPLICATION_ORCHADMIN: (ORCHADMIN_PROFILE,),
    APPLICATION_DISTRO_SANDBOX: (DISTRO_DEV_PROFILE,),
    APPLICATION_SETTINGS: (SETTINGS_PROFILE,),
    APPLICATION_ABACUS: (ABACUS_PROFILE,),
    APPLICATION_CONTENT: (CONTENT_PROFILE,),
    APPLICATION_COLLABORATOR: (COLLABORATORS_PROFILE,),
    APPLICATION_SONGWHIP: (SONGWHIP_PROFILE,),
    APPLICATION_NR: (NR_PROFILE,),
    APPLICATION_DOCUMENTS: (DOCUMENTS_PROFILE,),
}

PROFILE_TO_RESOURCE_RELATIONSHIP = 'HAS_ACCESS_TO'
RESOURCE_SUBACCOUNT = 'SubAccount'
RESOURCE_VENDOR = 'Vendor'

IDENTITY_USER_TYPE = ['label', 'artist', 'employee']

MOCK_USER_IDENTITIES = {
    '5efcd6d0a199c000143dd3fc',  # DEV mwalker@theorchard.com distro app
    '5c3fc338604bd70ff5f976fb',  # DEV jpenner@theorchard.com distro app
}

# Ows Notifications
OWS_NOTIFICATIONS = 'ows-notifications'
SOCIAL_SPIKE_SETTING = {
    'notification_type': 'push_notifications',
    'feed_type': 'social_spike'
}
TRENDING_TRACKS_SETTING = {
    'notification_type': 'push_notifications',
    'feed_type': 'trending_tracks'
}
PLAYLIST_PLACEMENT_SETTING = {
    'notification_type': 'push_notifications',
    'feed_type': 'playlist_placements'
}
DEFAULT_NOTIFICATION_SETTINGS = [
    SOCIAL_SPIKE_SETTING,
    PLAYLIST_PLACEMENT_SETTING,
    TRENDING_TRACKS_SETTING
]
DEFAULT_NOTIFICATION_PROFILE_TYPES = [
   ARTIST_PROFILE,
   INSIGHTS_PROFILE,
   LABEL_PROFILE
]
ERROR_CODE_OWS_NOTIFICATIONS_REQUEST = 'ows_notifications_error'


# DB constants
NEO4j_READ_ACCESS = 'READ'
NEO4j_WRITE_ACCESS = 'WRITE'


# The profiles supported when returning the applications list
APPLICATIONS_SUPPORTED_PROFILES = [
    INSIGHTS_PROFILE,
    LABEL_PROFILE,
    MONEYHUB_PROFILE,
    SETTINGS_PROFILE,
    COLLABORATORS_PROFILE,
    CONTENT_PROFILE,
    SONGWHIP_PROFILE,
    NR_PROFILE,
    DOCUMENTS_PROFILE
]

# neo4j Profile role types

# All Roles
# if you are adding a role here, it's probably needed in
# graphql-product/src/schema/schema.graphql also
CATALOG_ROLE = 'catalog'
MARKETING_ROLE = 'marketing'
ANALYTICS_ROLE = 'analytics'
ADMINISTRATOR_ROLE = 'administrator'
ACCOUNTING_ROLE = 'accounting'
MANAGE_RIGHTS_ROLE = 'manage_rights'
ADVERTISING_ROLE = 'advertising'
PRODUCER_ROLE = 'producer'
ADMIN_ROLE = 'admin'
NETWORK_ADMIN_ROLE = 'network-admin'
READ_ONLY_PRODUCER_ROLE = 'read-only-producer'
ROYALTIES_ROLE = 'royalties'
PAYMENTS_ROLE = 'payments'
NR_ROLE = 'neighbouring_rights'
DOCUMENTS_ROLE = 'documents'

PROFILE_ROLE_TYPES = [
    ACCOUNTING_ROLE, ADMIN_ROLE, ADMINISTRATOR_ROLE,
    ADVERTISING_ROLE, ANALYTICS_ROLE, CATALOG_ROLE,
    'insight', MANAGE_RIGHTS_ROLE, MARKETING_ROLE, PRODUCER_ROLE, NETWORK_ADMIN_ROLE,
    READ_ONLY_PRODUCER_ROLE, ROYALTIES_ROLE, PAYMENTS_ROLE, NR_ROLE, DOCUMENTS_ROLE
]

# All Brands

ORCHARD_BRAND = 'orchard'
SONY_BRAND = 'sme'
OVERDRIVE_BRAND = 'overdrive'
AWAL_BRAND = 'awal'

BRAND_TYPES = [
    ORCHARD_BRAND,
    SONY_BRAND,
    OVERDRIVE_BRAND,
    AWAL_BRAND
]
