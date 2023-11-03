# -*- coding: utf-8 -*-
"""ETL PIPELINE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FSZSSP_fz6cigU9lCUJ6L3g3r_oIFQpJ

# **DATA EXTRACTION**
"""

# Import Pandas and SQL Alchemy as libraries that would be used in Creating ETL's

import pandas as pd
import sqlalchemy as db

#Creating a variable for the link

url = 'https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx'

#importing it to python

df = pd.read_excel(url)
df.head()

"""# **DATA TRANSFORMATION**"""

#to check for null values

df.isna().values

df.isna().values.any()        #output will be in true or false

# to check for the data type

df.dtypes

# to see all the columns

df.columns

#to drop the segment column

df.drop(columns = 'Segment', inplace = False)

df.shape

"""# **LOADING THE DATA TO DATABASE**"""

#Sql instance

engine = db.create_engine('postgresql://sfqyhmdx:20WZYfNg-ipL-DbYv8XyYFKXq1uWkHJn@surus.db.elephantsql.com/sfqyhmdx')

df.to_sql('Financial_Data', engine,
                  if_exists='replace',
                  index=False,
                  method='multi')