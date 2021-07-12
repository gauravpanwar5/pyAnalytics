# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 08:18:55 2021

@author: Gaurav
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
 mtcars = data('mtcars')
df=mtcars
df
df.mpg.sort_values()
 intervals = np.linspace(0, 1, 11)
df.quantile(q=0.5, axis=0)
df.quantile(q=intervals, axis=0)

df.boxplot()
df.boxplot(column=['mpg']) 
ax = sns.stripplot(x="gear", y="mpg", data=df)

df.mpg
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.stripplot(x="gear", y="mpg" data=df)
ax = sns.boxplot(x=, y="total_bill", data=tips, showfliers = False)
ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

plt.show()
q3, q1 = np.percentile(df['hp'],[60, 25])
q3, q1
q3 - q1

from scipy import stats 
IQR = stats.iqr(df['hp'])
IQR
#define function to calculate interquartile range
def find_iqr(x): return np.subtract(*np.percentile(x, [60 , 25]))
#calculate IQR for rating and points column
df[['mpg', 'wt', 'hp']].apply(find_iqr)
df.apply(find_iqr)
#outliers
mpgZ = stats.zscore(df['mpg'])
len(mpgZ)
np.abs(mpgZ)
np.abs(mpgZ) > 2 #true or fALSE

np.where(np.absdfz(mpgZ) > 1)
dfz = np.abs(stats.zscore(df))
dfz
dfz[:, 0] #1st column
dfz[:, 0] == np.abs(mpgZ)
threshold = 3
dfz > threshold
print(np.where(dfz > threshold))
#skewness
skewValue = df.skew()
skewValue
#Kuutosis
kT = df.kurtosis()
kT
#paridhi
import pandas as pd
import numpy as np
import numpy as np
from scipy.stats import kurtosis, skew
from pydataset import data
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mtcars=data('mtcars')
data=mtcars
data
data.columns
skew(data, axis=0)
kurtosis(mtcars.hp)
#for hp; SKEW = 0.799407, kurtosis=0.275212
df.hp
df.mean
df.median
df.max
df.min
df.describe()
#sahil
dataDF = mtcars
dataDF.skew()
dataDF.kurtosis()
