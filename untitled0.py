# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:07:48 2021

@author: Gaurav
"""

id()mport pandas as pd
#link https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk/edit#gid=1858159025

student = pd.read_csv('https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk' + '/export?gid=1858159025&format=csv',  index_col=0 )
student.head(5)
student.shape
type(student)
