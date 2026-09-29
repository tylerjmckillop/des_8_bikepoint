from modules.loginitialise import setup_logging
from modules.bikepoint_extract_modularised import extract 
from modules.bikepoint_load_modularised import load_files_to_s3
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

logger = setup_logging('logs', dt.now().strftime('%Y-%m-%d %H-%M-%S'))

extract = extract('data', 'https://api.tfl.gov.uk/BikePoint/', dt.now().strftime('%Y-%m-%d %H-%M-%S'), 5, 10)

load = load_files_to_s3('data', os.getenv('AWS_ACCESS_KEY'), os.getenv('AWS_SECRET_ACCESS_KEY'), os.getenv('AWS_BUCKET_NAME'))