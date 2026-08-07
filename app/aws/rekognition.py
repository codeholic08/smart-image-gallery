import boto3
from config import Config

rekognition_client = boto3.client('rekognition', region_name=Config.AWS_REGION)

def detect_labels(filename):
    try:
        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': Config.S3_BUCKET, 'Name': filename}},
            MaxLabels=10
        )
        return [label['Name'] for label in response['Labels']]
    except Exception as e:
        raise Exception(f"Failed to detect labels: {str(e)}")