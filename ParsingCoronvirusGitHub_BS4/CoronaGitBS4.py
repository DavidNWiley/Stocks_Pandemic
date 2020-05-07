# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:16:50 2020

@author: Nick
"""


import pandas as pd
import requests as rq
import numpy as np
from bs4 import BeautifulSoup
from csv import reader
from datetime import datetime

# Using the new dataset url
url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

# using requests to get the html text
url_text = rq.get(url).text

# using the bs4 package to parse the url
soup = BeautifulSoup(url_text, "lxml")

# looking for the table that contains the coronavirus data
global_table = soup.find("table", attrs={"class", "highlight tab-size js-file-line-container"})

# begin parsing the table by 'tr' tags
global_table_data = global_table.find_all("tr")


data = []

# looping through the table in the 'tr' tag
for tr in global_table_data:
    td = tr.find_all('td', attrs={'class', 'blob-code blob-code-inner js-file-line'})
    
    # pulling each row of data from the table
    for t in td:
        sentence = [t.text]
        
        # Since the row is a single string, I use csv reader to parse the string and return a list
        for item_list in reader(sentence):
            
            # appending each row list to the data list to be converted into a dataframe
            data.append(item_list)

# creating the dataframe from the list of lists
df = pd.DataFrame(data[1:], columns=data[0])

# creating a list of column names that will NOT be unpivoted, this is because the confirmed dates in the data are columns, not rows
melt_column_names = ['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key']

# Will use these functions to change data types for excel
def convert_float(x):
    try:
        return float(x)
    except:
        return np.NaN
    
    
def convert_int(x):
    try:
        return int(x)
    except:
        return np.NaN

# unpivoted the date columns have the dates in a single column
new_df = df.melt(id_vars= melt_column_names, var_name='Date', value_name='Confirmed')

# changing the dataframe data types from objects to strings
for column in new_df.columns:
    new_df[column] = new_df[column].astype('string')

# changing non-string data types into their respective data types
# This makes working with the excel file a lot easier
new_df['Date'] = new_df.Date.apply(lambda x: datetime.strptime(x, "%m/%d/%y"))
new_df['UID'] = new_df.UID.apply(lambda x: convert_float(x))
new_df['code3'] = new_df.code3.apply(lambda x: convert_float(x))
new_df['FIPS'] = new_df.FIPS.apply(lambda x: convert_float(x))
new_df['Confirmed'] = new_df.Confirmed.apply(lambda x: convert_int(x))
new_df['Lat'] = new_df.Lat.apply(lambda x: convert_float(x))
new_df['Long_'] = new_df.Long_.apply(lambda x: convert_float(x))

# writing the excel file
new_df.to_excel('/home/david/python_files/ImpactofCoronaVirus_Stocks/ParsingCoronvirusGitHub_BS4/US_COVID19_Confirmed.xlsx', index=False)





