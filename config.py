import os

class Config:
    AWS_REGION = '<AWS_REGION>'
    S3_BUCKET = '<S3_BUCKET>'
    ES_HOST = '<ES_HOST>'
    ES_INDEX = '<ES_INDEX>'
    LEX_BOT_ID = '<BOT_ID>'
    LEX_BOT_ALIAS_ID = '<BOT_ALIAS_ID>'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')