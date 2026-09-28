# Import packages
import os
import boto3
from dotenv import load_dotenv 

# Obtain .env variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Set up S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# Upload file using a dummy
file_to_upload = 'data/2026-09-23 17-00-10.json'
file_name_s3 = '2026-09-23 17-00-10.json'

s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, file_name_s3)