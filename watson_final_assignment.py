import os
import glob
import json
import pandas as pd
from datetime import datetime

filepath = '/home/password/learn/python'
tmpfile = "temp.tmp"               # file used to store all extracted data
logfile = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored

#!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_1.json"
#!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_2.json"
#!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/exchange_rates.csv"


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


columns = ['Name', 'Market Cap (US$ Billion)']


def extract():
    # create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=columns)
    # process all json files
    jsonfile = glob.glob("bank_market_cap_1.json")
    f = open(jsonfile[0], "r")
    data = extract_from_json(f)
    extracted_data = extracted_data.append(data, ignore_index=False)
    return extracted_data


#data = extract()
# print(type(data))
# print(data)

csv_file = glob.glob("exchange_rates.csv")
csv_f = open(csv_file[0], "r")
csv_data = extract_from_csv(csv_f)
# print(type(csv_data))
# print(csv_data.info())


def get_fxrate(ccy_cd):
    csv_file = glob.glob("exchange_rates.csv")
    csv_f = open(csv_file[0], "r")
    csv_data = extract_from_csv(csv_f)
    exchange_rate = 'NOT FOUND'
    for i, val in csv_data.iterrows():
        if(val[0] == ccy_cd):
            exchange_rate = val[1]
    return exchange_rate

# print(exchange_rate)


def transform(target_base_ccy, precision):
    # Write your code here
    usd_df = extract()
    result = usd_df.copy()
    exch_rt = get_fxrate(target_base_ccy)
    result['Market Cap (US$ Billion)'] = (
        result['Market Cap (US$ Billion)'] * exch_rt).round(precision)
    result.rename(columns={'Market Cap (US$ Billion)':
                           'Market Cap (GBP$ Billion)'}, inplace=True)
    return result


res = transform('GBP', 3)
print(type(res))
res.to_csv('bank_market_cap_gbp.csv', index=False)
# Manojavam!23
#satya@ipivot.io, hr@ipivot.io
#Django for Python as Hibernate for Java
# IBM Cloud Feature : dfa7167f927b088baf2aa9285d42fa6f
#data in motion
#data as service
