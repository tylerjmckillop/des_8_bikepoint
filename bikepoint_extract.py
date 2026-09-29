#Import the packages required

import requests
import os 
import json 
from datetime import datetime as dt
import time
import logging

#API endpoint we want to extract the data from 
url = 'https://api.tfl.gov.uk/BikePoint/'


#Create a folder for our extracted data if it doesn't already exist
#If it finds something called data_dir it is ok
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)



#Create a timestamp so each extract gets a unique filename 
timestamp = dt.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'
#Save in data dictionary folder, then save the file with the name of the timestamp variable, and save as json

#Make a folder for log files if it doesn't already exist
log_dir = 'log'
os.makedirs(log_dir, exist_ok = True)
log_filename = f'{log_dir}/{timestamp}.log'


#Configure logging so messages are written to the log file
logging.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
    #Base level is info
)

#Create the logger and confirm that is has been successfully set up 
logger = logging.getLogger()
logger.info('Logger successfully initialised')

#Setup a while loop to keep trying in case the API fails
max_retry = 5
attempt = 0
delay = 10

while attempt < max_retry:



#Send a GET request to the API. Use the requests library to get the url and save it as variable response
    response = requests.get(url)


#Write an if statement based on status code
    status = response.status_code
    if 200 <= status < 300:
    

#Convert the JSON response into Python variable
        data = response.json()

        #Check that API has returned data

        if len(data) > 0:
            try:


#Open the output file and write the API data to it as JSON
#Looks at the file we created as a variable, and then we are dumping the data into the file that we just created
                with open(filename, 'w') as file:
                    json.dump(data, file)

            #Print that the filename was successfully saved
                print(f'{filename} was successfully saved')
                logger.info(f'{filename} was successfully saved') #What we see in our logger, .info just information and what is inside the string is the output
                break
            except Exception as e:
                print(f'An error has occured: {e}')
                logger.error(f'An error has occured: {e}')
            break
        #Write an else statement if no data is there
        else:
            print("No data has been retrieved")
            logger.warning("No data has been retrieved")
            break

    #If in this bracket then we try again until the status_code reaches the number we want/reach max_retry
    elif status < 200 or status >= 500:
        time.sleep(delay)
        attempt += 1
        print(f'Status code {status}. Retrying attempt number {attempt}')
        logger.info(f'Status code {status}. Retrying attempt number {attempt}')
 
    else:
        print(f'Error. Status code {status}. Fix it')
        logger.critical(f'Error. Status code {status}. Fix it')
        break