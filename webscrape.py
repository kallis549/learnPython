import requests
import os 
from PIL import Image
#from IPython.display import IFrame
from randomuser import RandomUser
import pandas as pd

url='https://www.ibm.com/'
r=requests.get(url)
print(r.status_code)
print(r.request.headers)
print("request body : ", r.request.body)

header = r.headers
print(r.headers)
print(header['date'])
print(header['Content-Type'])
print(r.encoding)
print(r.text[0:100])

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
s=requests.get(url)
print(s.headers)
print("request body : ", s.request.body)
print(s.request.headers)
print(s.headers['Content-Type'])

################################
######### GET METHOD ###########
################################

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
print(r.json())

################################
######### POST METHOD ##########
################################

url_post='http://httpbin.org/post'
layload={"name":"Barkhurdar","ID":"23423423"}
r_post=requests.post(url_post,data=layload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print(r_post.json()['form'])

