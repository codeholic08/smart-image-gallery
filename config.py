import os

class Config:
    AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
    S3_BUCKET = os.environ.get('S3_BUCKET', '')
    ES_HOST = os.environ.get('ES_HOST', '')
    ES_INDEX = os.environ.get('ES_INDEX', '')
    LEX_BOT_ID = os.environ.get('LEX_BOT_ID', '')
    LEX_BOT_ALIAS_ID = os.environ.get('LEX_BOT_ALIAS_ID', '')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'unset')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'unset')