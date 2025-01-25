import boto3
import os

bucket_name = os.getenv('MINIO_BUCKET_NAME')
aaki = os.getenv('MINIO_ACCESS_KEY')
asak = os.getenv('MINIO_SECRET_KEY')
s3 = boto3.client('s3', 
                  endpoint_url='http://minio:9000', 
                  aws_access_key_id=aaki, 
                  aws_secret_access_key=asak)
"""
try:
    s3.create_bucket(Bucket=bucket_name)
except:
    pass
"""
def upload_file(file_name, object_name):
    extra_args = {'ACL': 'public-read', 'ContentType': 'image/png', 'ContentDisposition': 'inline'}
    s3.upload_file(file_name, bucket_name, object_name, ExtraArgs=extra_args)