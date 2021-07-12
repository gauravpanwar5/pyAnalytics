# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:06:24 2021

@author: Gaurav
"""

url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
import pandas as pd
df = pd.read_csv(url)
df                 
df.columns
df.shape
df.columns
df.head(n=3)
import numpy as np
import matplotlib.pyplot as plt
len(df)
df.describe()
df.dtypes
df['cost'] = df['cost'].astype('category')
df.describe()

pd.options.display.float_format='{:.2f}'.format
df.region.value_counts().plot(kind='bar')
df.custname.value_counts()
 df.sort_values(['custname'])
df.custname.value_counts()
df.custname.value_counts()
df.custname.value_counts().sort_values(ascending=True).head(5)
 df.groupby('partnum').revenue.sum().sort_values(ascending=False).head(5)
df[['partnum','revenue']].sort_values(by='revenue',ascending=False).head(5)
df.groupby('partnum')_sort_values(ascending=False )
df.groupby('custname')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).head(5)
df.partnum.values_counts()
df[['revenue','region']].groupby('region').sum().sort_values(by='revenue',ascending=False).head(5).plot(kind='barh')
