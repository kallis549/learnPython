from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd
import json

url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=EDa4W6F6JSFmipFI7qY6PqNoGLWYyxAD"
r = requests.get(url)
data = json.loads(requests.get(url).text)# print(data['rates'])
curr_dict = data['rates']
curr_df = pd.DataFrame.from_dict(curr_dict, orient='index', columns=['Rate'])
print(curr_df)
curr_df.to_csv('mydata.csv', index=True )
