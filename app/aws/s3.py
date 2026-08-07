import boto3
from botocore.exceptions import ClientError
import json
from config import Config

s3_client = boto3.client('s3', region_name=Config.AWS_REGION)

def upload_file(file, custom_labels):
    try:
        s3_client.upload_fileobj(
            file,
            Config.S3_BUCKET,
            file.filename,
            ExtraArgs={
                "Metadata": {"x-amz-meta-customlabels": json.dumps(custom_labels)}
            }
        )
    except ClientError as e:
        raise Exception(f"Failed to upload file to S3: {str(e)}")