# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:09:11 2021

@author: Gaurav
"""
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree

url = url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/diabetes.csv'

data = pd.read_csv(url)
data.head()
data.columns
