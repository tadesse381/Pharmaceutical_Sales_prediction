#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error


# In[ ]:


conn = mysql.connect(host='localhost', user='root', password='root')
cur = conn.cursor()
print(conn) # it will print a connection object if everything is fine
#Here we create a Database
cur.execute(f"CREATE DATABASE IF NOT EXISTS pharmaceutical;")
dbQuery = f"ALTER DATABASE pharmaceutical CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
cur.execute(dbQuery)
conn.commit()


# In[ ]:


#Create a connection with DBName
db_dbname = mysql.connect(host='localhost', user='root', password='root',database = "pharmaceutical")
print(db_dbname) # it will print a connection object if everything is fine
cursor = db_dbname.cursor()
#Create a table with a Primary Key
cursor.execute("CREATE TABLE PharmaceuticalInformetion(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,Store INT,DayOfWeek INT,Date DATE,Sales INT,Customers INT,Open INT,Promo INT,StateHoliday DATE, SchoolHoliday INT,Year INT, Month INT, Day INT,WeekOfYear INT,SalePerCustomer FLOAT,StoreType VARCHAR(1000),Assortment VARCHAR(1000),CompetitionDistance FLOAT,CompetitionOpenSinceMonth FLOAT, CompetitionOpenSinceYear FLOAT,Promo2 INT,Promo2SinceWeek VARCHAR(1000),Promo2SinceYear VARCHAR(1000),PromoInterval VARCHAR(1000),StateHoliday VARCHAR(1000)")

## 'DESC table_name' is used to get all columns information
cursor.execute("DESC PharmaceuticalInformetion")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())

# In[ ]:

#import data from a CSV file and Print It to Check
tweetinformation=pd.read_csv('data/processed_tweet_data.csv')
tweetinformation.head()


# In[ ]:


#loop through the data frame
for _,row in tweetinformation.iterrows():
    #here %S means string values
    sql = "INSERT INTO pharmaceutical.PharmaceuticalInformetion VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlQuery = f"""INSERT IGNORE INTO PharmaceuticalInformetion(Store,DayOfWeek,Date,Sales,Customers,Open,Promo,StateHoliday,SchoolHoliday,Year,Month,Day,WeekOfYear,SalePerCustomer,StoreType,Assortment,CompetitionDistance,CompetitionOpenSinceMonth ,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek,Promo2SinceYear,PromoInterval,StateHoliday)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12], row[13], row[15],row[16],row[17], row[18], row[19],row[20],row[21],row[22], row[23], row[24])
    # Execute the SQL command
    cursor.execute(sqlQuery, data)
    cursor.execute(sql, tuple(row))
    print("Record inserted")


# In[ ]:


## defining the Query
query = "SELECT * FROM PharmaceuticalInformetion"
## getting records from the table
cursor.execute(query)
## fetching all records from the 'cursor' object
records = cursor.fetchall()
## Showing the data
for record in records:
    print(record)

