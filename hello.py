import requests

URL = "https://football-data.co.uk/englandm.php"
page = requests.get(URL)

print(page.text)



#import requests
#from bs4 import BeautifulSoup

#URL = "print(results.prettify())"
#page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
#print(results.prettify())