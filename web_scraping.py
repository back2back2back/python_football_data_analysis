
import pandas as pd 
from datetime import datetime
import numpy as np


import requests
from bs4 import BeautifulSoup

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
            #if url.__contains__('/2'):  
                if not url.__contains__('/21'): 
                    if not url.__contains__('/04'):  
                        list_of_urls.append('https://football-data.co.uk/'+url)
        #print (list_of_urls)
else:
    print("Error:", response.status_code)

array_list = np.array(list_of_urls)
unique_list = np.unique(array_list)
print(unique_list)

current_date = pd.to_datetime('today').normalize()
date_range = pd.date_range(start='2010-8-1',end=current_date,name= "Date")
df = pd.DataFrame.from_dict(date_range)

result = pd.DataFrame(columns=['Date'])#,'F','G','H','I','J'])
result['Date']=date_range
print (result)


for url in unique_list:
    data= pd.read_csv(url,usecols=[0,1,2,3,4])#,5,6,7,8,9,10])
    data.Date = pd.to_datetime(data .Date, format= 'mixed')
    pd.merge(result,data,how='left',on='Date')
    print(result)

print(result)

result.to_csv("test_data_eng_1.csv",index=False)
#data.Date = pd.to_datetime(data.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')


'''


#create date range to join all tables onto
current_date = pd.to_datetime('today').normalize()
date_range = pd.date_range(start='2010-8-1',end=current_date,name= "Date")
# get data 
#print(date_range)
current_year = int((datetime.now().strftime('%y')) + str(int(datetime.now().strftime('%y'))+1))
min_year = 1112

prem_source = 'https://football-data.co.uk/mmz4281/' + str(min_year-101) +'/E0.csv'
champ_source = 'https://football-data.co.uk/mmz4281/' + str(min_year-101) +'/E1.csv'
l1_source = 'https://football-data.co.uk/mmz4281/' + str(min_year-101) +'/E2.csv'
l2_source = 'https://football-data.co.uk/mmz4281/' + str(min_year-101) +'/E3.csv'

data_prem = pd.read_csv(prem_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
data_prem.Date = pd.to_datetime(data_prem.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
data_champ = pd.read_csv(champ_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
data_champ.Date = pd.to_datetime(data_champ.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
data_l1 = pd.read_csv(l1_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
data_l1.Date = pd.to_datetime(data_l1.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
data_l2 = pd.read_csv(l2_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
data_l2.Date = pd.to_datetime(data_l2.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')

for year_var in range (min_year,current_year,101):
    year_var_str = str(year_var)
    prem_source = 'https://football-data.co.uk/mmz4281/' + year_var_str +'/E0.csv'
    data_prem_new = pd.read_csv(prem_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
    data_prem_new.Date = pd.to_datetime(data_prem_new.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
    data_prem = pd.concat([data_prem,data_prem_new],ignore_index = True)
 
for year_var in range (min_year,current_year,101):
    year_var_str = str(year_var)   
    champ_source = 'https://football-data.co.uk/mmz4281/' + year_var_str +'/E0.csv'
    data_champ_new = pd.read_csv(champ_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
    data_champ_new.Date = pd.to_datetime(data_champ_new.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
    data_champ = pd.concat([data_champ,data_champ_new],ignore_index = True)
    
for year_var in range (min_year,current_year,101):
    year_var_str = str(year_var)
    l1_source = 'https://football-data.co.uk/mmz4281/' + year_var_str +'/E0.csv'
    data_l1_new = pd.read_csv(l1_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
    data_l1_new.Date = pd.to_datetime(data_l1_new.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
    data_l1 = pd.concat([data_l1,data_l1_new],ignore_index = True)

for year_var in range (min_year,current_year,101):
    year_var_str = str(year_var)
    l2_source = 'https://football-data.co.uk/mmz4281/' + year_var_str +'/E0.csv'
    data_l2_new = pd.read_csv(l2_source,usecols=[0,1,2,3,4,5,6,7,8,9,10])
    data_l2_new.Date = pd.to_datetime(data_l2_new.Date, format= 'mixed')#'%Y-%m-%d', errors='coerce')
    data_l2 = pd.concat([data_l2,data_l2_new],ignore_index = True)

data = pd.concat([data_prem,data_champ,data_l1,data_l2],ignore_index = True)
print(data_prem)
print(data_champ)
print(data_l1)
print(data_l2)
print(data)

df = pd.DataFrame.from_dict(date_range)
result = pd.merge(df,data,how='left',on='Date')
result.to_csv("test_data_eng.csv",index=False)




import requests
from bs4 import BeautifulSoup

URL = "https://football-data.co.uk/englandm.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all('td')
print(results)


import os
from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve

URL = 'https://football-data.co.uk/englandm.php'
OUTPUT_DIR = ''  # path to output folder, '.' or '' uses current folder

u = urlopen(URL)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")



results = soup.find_all (<td>)
print(results.prettify())

for link in soup.select('a[href^="http://"]'):
    href = link.get('href')
    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx']):
        continue

    filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])

    # We need a https:// URL for this site
    href = href.replace('http://','https://')

    print("Downloading %s to %s..." % (href, filename) )
    urlretrieve(href, filename)
    print("Done.")
    '''