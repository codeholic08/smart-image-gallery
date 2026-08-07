import requests
from requests_aws4auth import AWS4Auth
from config import Config
from datetime import datetime

aws_auth = AWS4Auth(Config.AWS_ACCESS_KEY_ID, Config.AWS_SECRET_ACCESS_KEY, Config.AWS_REGION, 'es')

def search_photos(labels):
    es_query = {
        "query": {
            "terms": {
                "labels": labels
            }
        }
    }
    
    try:
        response = requests.get(f'{Config.ES_HOST}/{Config.ES_INDEX}/_search', auth=aws_auth, json=es_query)
        response.raise_for_status()
        results = response.json()['hits']['hits']
        return [f"https://{Config.S3_BUCKET}.s3.amazonaws.com/{hit['_source']['objectKey']}" for hit in results]
    except requests.RequestException as e:
        raise Exception(f"Failed to search Elasticsearch: {str(e)}")

def index_photo(filename, labels):
    es_document = {
        "objectKey": filename,
        "bucket": Config.S3_BUCKET,
        "createdTimestamp": datetime.now().isoformat(),
        "labels": labels
    }
    
    try:
        response = requests.post(f'{Config.ES_HOST}/{Config.ES_INDEX}/_doc', auth=aws_auth, json=es_document)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Failed to index in Elasticsearch: {str(e)}")