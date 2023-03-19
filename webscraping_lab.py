from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
r = requests.get(url)
# print(r.status_code)
# print(r.request.headers)
# print("request body : ", r.request.body)

html_data = requests.get(url).text
print(html_data[483:586])

soup = BeautifulSoup(html_data, "html.parser")
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    columns = row.find_all('td')
    str = ''
    list = {}
    for i, column in enumerate(columns):
        val = column.get_text().strip()
        if(i > 0):
            list[data.columns[i - 1]] = val
    # print(list)
    if(list):
        data = data.append(list, ignore_index=True)
print(data.head())
bank_market_cap = data.to_json()
print(bank_market_cap)
