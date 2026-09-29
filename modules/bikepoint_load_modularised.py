import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime as dt

# Obtain .env variables
load_dotenv()

def load(AWS_ACCESS_KEY: str, AWS_SECRET_ACCESS_KEY: str, AWS_BUCKET_NAME, data_dir:str):
    # Set up S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    # Make a folder for log files if it doesn't already exist

    timestamp = dt.now().strftime('%Y-%m-%d %H-%M-%S')

    log_dir = 'load_log'
    os.makedirs(log_dir, exist_ok = True)
    log_filename = f'{log_dir}/{timestamp}.log'


    # Configure logging so messages are written to the log file
    logging.basicConfig(
        filename = log_filename,
        format = '%(asctime)s - %(levelname)s -%(message)s',
        level = logging.INFO
    )

    # Create the logger and confirm that is has been successfully set up 
    logger = logging.getLogger(__name__)
    logger.info('Logger successfully initialised')

    # Upload every file in our data folder
    files_to_upload = os.listdir(data_dir)

    for file in files_to_upload:
        file_to_upload = f'data/{file}'
        try: 
            s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, file)
            print(f'{file} Uploaded successfully')
            logger.info(f'{file} successfully uploaded')
            os.remove(file_to_upload) # Remove the file
        except Exception as e:
            print(f'An error has occurred: {e}')
            logger.error(f'An error has occured: {e}')


    # Upload file using a dummy (do this before the upload every file in our data folder)
    # file_to_upload = 'data/2026-09-23 17-00-10.json'
    # file_name_s3 = '2026-09-23 17-00-10.json'

    # s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, file)