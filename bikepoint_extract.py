#Import the packages required

import requests
import os 
import json 
from datetime import datetime as dt

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


#Send a GET request to the API. Use the requests library to get the url and save it as variable response
response = requests.get(url)


#Write an if statement based on status code
status = response.status_code


#Convert the JSON response into Python variable
data = response.json()


#Print the status code that you get from the response
print(response.status_code)


#Open the output file and write the API data to it as JSON
#Looks at the file we created as a variable, and then we are dumping the data into the file that we just created
with open(filename, 'w') as file:
    json.dump(data, file)