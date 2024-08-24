
import pandas as pd
data = pd.read_csv('https://football-data.co.uk/mmz4281/2425/E0.csv')
print (data)

'''import requests

URL = "https://football-data.co.uk/englandm.php"
page = requests.get(URL)

print(page.text)




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