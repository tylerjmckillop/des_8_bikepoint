#Import the packages required

import requests
import os 
import json 
from datetime import datetime as dt
import time
import logging

def extract(data_dir: str, url: str, timestamp: str, max_retry: int, delay: int):
    """Extracts JSON

    Args:
        data_dir (str): Where you want to store the data
        url (str): The URL where you want to download JSON from
        timestamp (str): The filename will be this
        max_retry (int): The numer of times to retry the API
        delay (int): How long to wait between retries (seconds)
    """
    os.makedirs(data_dir, exist_ok = True)
    logger = logging.getLogger(__name__)
    filename = f'{data_dir}/{timestamp}.json'

    attempt = 0

    while attempt < max_retry:
        response = requests.get(url)
        status = response.status_code
        if 200 <= status < 300:
            data = response.json()

            if len(data) > 0:
                try:
                    with open(filename, 'w') as file:
                        json.dump(data, file)
                    print(f'{filename} was successfully saved')
                    logger.info(f'{filename} was successfully saved')
                    break
                except Exception as e:
                    print(f'An error has occured: {e}')
                    logger.error(f'An error has occured: {e}')
                break
            else:
                print("No data has been retrieved")
                logger.warning("No data has been retrieved")
                break

        elif status < 200 or status >= 500:
            time.sleep(delay)
            attempt += 1
            print(f'Status code {status}. Retrying attempt number {attempt}')
            logger.info(f'Status code {status}. Retrying attempt number {attempt}')
        else:
            print(f'Error. Status code {status}. Fix it')
            logger.critical(f'Error. Status code {status}. Fix it')
            break