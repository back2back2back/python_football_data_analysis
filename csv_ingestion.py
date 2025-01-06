import pandas  as pd
from web_scraping import unique_list

for url in unique_list:
    df= pd.read_csv(url,usecols=['Div','HomeTeam'])
     
print(df)