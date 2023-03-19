import requests
import json
import pandas as pd

data=requests.get('https://fruityvice.com/api/fruit/all')
results = json.loads(data.text)
#print(results)
pd.DataFrame(results)

df2=pd.json_normalize(results)
print(df2[['name','family']])

#print(df2.iloc[0]["name"])

#print(df2.iloc[0]["name"] == 'Orange')
#
#print(df2.loc[df2["family"] == 'Rosaceae'])

#cherry = df2.loc[df2["family"] == 'Rosaceae']
#for fruit in cherry.name:
    #print(fruit)
