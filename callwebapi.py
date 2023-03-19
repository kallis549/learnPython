import requests
import os 
from PIL import Image
#from IPython.display import IFrame
from randomuser import RandomUser
import pandas as pd

r=RandomUser()
print(r)

user_list = r.generate_users(10)
print(user_list)
name = r.get_full_name()
print(name)

for user in user_list:
    print(user.get_full_name()," ", user.get_email())


for user in user_list:
    print(user.get_full_name()," ", user.get_picture())

def get_users():
    users =[]

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})

    return pd.DataFrame(users)

df1 = pd.DataFrame(get_users())
print(df1)
