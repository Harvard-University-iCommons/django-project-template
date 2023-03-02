from .base import *

# tlt hostnames
ALLOWED_HOSTS = ['.tlt.harvard.edu']
ALLOWED_CIDR_NETS = [SECURE_SETTINGS.get('vpc_cidr_block')]


# Store static files in S3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = SECURE_SETTINGS.get('static_files_s3_bucket')
AWS_QUERYSTRING_AUTH = False
AWS_LOCATION = SECURE_SETTINGS.get('static_files_s3_prefix')
AWS_S3_CUSTOM_DOMAIN = 'static.tlt.harvard.edu'
AWS_DEFAULT_ACL = None
