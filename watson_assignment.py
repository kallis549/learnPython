import pandas as pd

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
# print(df.head())


xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()
# print(df.head())

x = df[['Rating']]
print(type(x))
print(df.index)

new_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#df = df.set_index(pd.Index(new_index))
# print(df.index)

df_new = df
df_new.index = new_index
print(df_new.index)
