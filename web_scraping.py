
import pandas as pd 
from datetime import datetime
import numpy as np


import requests
from bs4 import BeautifulSoup


import sqlite3

# Specify the URL you want to scrape
url = "https://football-data.co.uk/englandm.php"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <a> tags in the HTML
    links = soup.find_all('a')

    # Extract the href attribute from each link
    urls = [link.get('href') for link in links]

    list_of_urls = []
    # Print all the extracted links
    for url in urls:
        if any(url.endswith(x) for x in ['E0.csv']):
            if url.__contains__('/2'):  
                if not url.__contains__('/21'): 
                    if not url.__contains__('/04'):  
                        list_of_urls.append('https://football-data.co.uk/'+url)
        #print (list_of_urls)
else:
    print("Error:", response.status_code)

array_list = np.array(list_of_urls)
unique_list = np.unique(array_list)
print(unique_list)