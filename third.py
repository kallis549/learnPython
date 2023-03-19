import pandas as pd

df = pd.read_csv('./kal.dat')
print(df.head(5))
print(df.tail(5))

df = pd.read_csv('./covid19_deaths.dat', delimiter='|')
print(df.head(10))


df = pd.read_csv('./commodity_history.dat', delimiter='|')
##print header
print("HEAD 10")
print(df.head(10))
##print columns
print("COLUMNS")
print(df.columns)
##print data is specific columns
print("SPECIFIC COLUMNS")
print(df[['PSORG', 'PWHEAMT', 'PSILVER']])

##print rows in the range
print("RANGE OF ATTRIBUTES")
print(df.iloc[1:20])

##print a particular cell
print("PARTICULAR CELL")
print(df.iloc[13,0])

##iterate through a dataframe
#for index, row in df.iterrows():
#	print(index, row)


##iterate through a dataframe
print("ITERATE AND PRINT WITH CONDITION")
for index, row in df.iterrows():
	if (row['PPOTASH'] > 115):
		print(index, row['Commodity'])	
		#print(index, row)


##locate/search
print("LOCATE WITH CRITERIA")
print(df.loc[df['Commodity'] == "2020M1"])

## 
print("HIGHLEVEL STATS")
print (df.describe())

##
print("SORTIGN BY COLUMN")
print(df.sort_values(['PTOMATO'], ascending=True))

##
print("SORTING BY MULTIPLE COLUMNS")
print(df.sort_values(['Commodity','PTOMATO'], ascending=[0,1]))

##Add new column 
print("ADD NEW COLUMN IN DATAFRAME")
df['TOTAL'] = df['PPOTASH']+df['PDAP']+df['PNFUEL']+df['PFANDB']+df['PFOOD']
cols = list(df.columns)
df = df[cols[0:1] + [cols[-1]] + cols[1:90]]
print(df.head(5))
#df.drop(columns=['TOTAL']).head(5)
#print(df.drop(columns=['TOTAL']).head(5))

#Another way to add new column - with SUM
df['KALLIS'] = df.iloc[:, 81:84].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:1] + [cols[-1]] + cols[1:90]]
print(df.head(5))

df.to_csv('./modified_dat.csv', index=False, sep="|")



newdf = pd.read_csv('./covid19_cases.csv', delimiter='|')
newdf.fillna(0, inplace=True)
print(newdf.head(5))
print(newdf.tail(5))

## replace NaN with zero

fltrd_df = newdf.loc[(newdf['travel_history_location'] == 'Wuhan') & 
		(newdf['sex'] == 'female') & (newdf['province'] == 'Ontario')]
print(fltrd_df)
print(fltrd_df.reset_index(drop=True))

for index, col in newdf.iteritems():
	if (index == 'city'):
		print (index, col)
