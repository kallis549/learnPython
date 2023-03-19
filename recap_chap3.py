import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
print (d)

ser = pd.Series(my_data, labels)
print (ser)
print (pd.Series(arr,labels))
print (pd.Series(labels))

print (pd.Series(data=[sum, print, len]))

ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
print (ser1)

ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])
print (ser2)

print (ser1['USA'])

print (ser1 + ser2)

#########DATA FRAMES##########

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print (df)
print(df['X'])
print(df[['X','Z']])

df['new'] = df['W'] + df['Z']
print (df)
arr = df.drop('new', axis=1)
print (arr)
print (df)

arr = df.drop('A', axis=0, inplace=True)
print (df)

print(df.loc['B'])
print(df.iloc[1])
print(df.loc['B','Y'])

print(df.loc[['C','B'],['X','Y']])

dfrm = pd.DataFrame(randn(8,7), 
					['A','B','C','D','E','F', 'G', 'H'], 
					['T','U','V','W','X','Y','Z'])
print (dfrm)
print (dfrm > 0)
print (dfrm[dfrm > 0])
print (dfrm[dfrm['X'] > 0])
print ("@@@@@@@@@@@@@")
print (dfrm[dfrm['X'] > 0][['T','U','Z']])

print ("@@@@@@@@@@@@@")
print (dfrm[(dfrm['X'] > 0) & (dfrm['Z'] > 1)][['T','U','Z']])

print(dfrm.reset_index())	
dfrm['work'] = 'PRGMR TL PL PM TSTR QA APPR USR'.split()
print (dfrm.set_index('work'))
print (dfrm)


