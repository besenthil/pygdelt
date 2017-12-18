# -*- coding: utf-8 -*-

##
# All global settings for the downloader are configured in this file
##


# URL of the GDELT site to download the files
GDELT_URL = 'http://data.gdeltproject.org/events/'

GDELT_ZIP_FILE_EXTENSION_PATTERN = \
    { 'daily': '.export.CSV.zip',
      'monthly':'.zip',
      'yearly':'.zip',
    }

# If you are behind a proxy, specify it in this format "'http':'hostname:port'"
PROXY_SERVERS = dict()

# Path of the folder where you want to store the downloaded files, if you dont want to store in s3
DOWNLOAD_DIRECTORY = '/home/senthil/code/turi/gdelt/data/'

# Max file size in MB beyond which you will restrict download
TOO_LONG_IN_MB =100000000000

# AWS Access Settings - s3 & dynamodb
USE_CDC_HANDLER = False
AWS_ACCESS_KEY_ID = '123'
AWS_SECRET_ACCESS_KEY = '456'
REGION_NAME = 'regioname'
BUCKET_NAME = 'bucket_name'
KEY_PREFIX = 'key_prefix_name'

DOWNLOAD_TIME_OUT = 5

VERBOSE=True
