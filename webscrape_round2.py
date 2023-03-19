from bs4 import BeautifulSoup # this module helps in web scrapping.

import requests
import numpy as np

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

print(two_tables_bs.find('table', class_='pizza'))

url="http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a',href=True):
    print(link.get('href'))

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

var='01234567'
print(var[::2])
print(var.find('3'))
print(1//2)
print(2/2)

B=[1,2,3,4,5]
b=set(B)
#print(b)



x=6
if(x!=1):
 print('How are you?')
else:
 print('Hi')

def add(x): return(x+x)
print(add('1'))

B=[7,2,9,4,5]
print(sorted(B))

A=['1','2','3']
for a in A:
    print(2*a)



for i in range(1,5):
    if (i!=2):
        print(i)

a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
print(a+b)


a=np.array([1,1,1,1,1])
print(a+10)


