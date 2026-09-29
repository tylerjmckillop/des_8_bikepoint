from modules.loginitialise import setup_logging
from modules.bikepoint_extract_modularised import extract 
from datetime import datetime as dt

logger = setup_logging('logs', dt.now().strftime('%Y-%m-%d %H-%M-%S'))

extract = extract('data', 'https://api.tfl.gov.uk/BikePoint/', dt.now().strftime('%Y-%m-%d %H-%M-%S'), 5, 10)