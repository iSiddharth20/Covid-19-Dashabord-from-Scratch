#!/usr/bin/python3

# Importing Libraries
import requests 
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Web Scrapping
URL = 'https://www.mohfw.gov.in/'								# Declaring the URL
web_data = requests.get(URL)									# Getting data from website
raw_data = BeautifulSoup(web_data.content, "html.parser")		# Processing known data to get HTML format
thead = raw_data.find_all('thead')[-1]							# Finding all <th> tags
head = thead.find_all('tr')										# Finding all <tr> tags
tbody = raw_data.find_all('tbody')[-1]
body = tbody.find_all('tr')

# Getting the data into Pandas Data Frame
head_rows = []
body_rows = []
for tr in head:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    head_rows.append(row)  
for tr in body:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    body_rows.append(row)
df_final = pd.DataFrame(body_rows[:len(body_rows)-2], columns=head_rows[0])   
df_final.drop('S. No.', axis=1, inplace=True)
# Renaming Columns
df_final.columns = ['Name of State/UT' , 'Active Cases', 'Cured/Migrated/Discharged', 'Death(s)', 'Total Registered Cases']
df_final = df_final[:-3]
df_final.drop(df_final.tail(1).index,inplace=True)

now = datetime.now()
# Creating CSV File with Custom File Name as per Time
path = '../DailyData/'
filename = now.strftime("%m%d")+'.csv'
df_final.to_csv(path+filename, index=False)
df_final = pd.read_csv(path+filename)
df_final_sum = df_final.sum()[1:]

# Storing when was the data last updated
last_update = now.strftime("%d %B, %I:%M %p")