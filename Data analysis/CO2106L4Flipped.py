#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
from scipy.optimize import curve_fit


# In[2]:


conf = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
confi = pd.read_csv(conf) #read the data and stores into a dataframe 


# In[3]:


# first 5 rows and last 5 rows would be tail(5)
confi.head(5)


# In[4]:


# shape is the number of rows and columns
confi.shape


# In[5]:


# Summary of missing values
confi.isnull().sum()


# In[6]:


grouped_conf = confi.groupby(by=['Country/Region']).sum()
grouped_conf


# In[7]:


grouped_conf.shape


# In[8]:


# Total number of confirmed cases for the UK
country = confi['Country/Region']=='United Kingdom'
total = confi[country].iloc[:, 4: ] # grap all the cases for the different regions of the UK
print('subtotals over time ', total)
total = total.apply(sum, axis=0) # sum over the rows
print('Total over time ', total)
# Total cases for the UK
print('Total confirmed cases to date is', total[-1])


# In[9]:


# sorting
sorted_grouped_conf = grouped_conf.sort_values(by=grouped_conf.columns[-1], ascending=False)
sorted_grouped_conf.head(20)


# In[10]:


# Bar chart
last_col = confi.iloc[-1]
last_day = last_col.index[-1]
plt.figure(figsize=(12, 8))
plt.title('Top 10 countries with highest confirmed cases', fontsize=14)
plt.barh(sorted_grouped_conf[last_day].index[:10],        sorted_grouped_conf[last_day].head(10))
plt.xlabel('Total cases by '+last_day)
plt.grid()
plt.show()


# In[11]:


# Bar chart using Seaborn
last_col = confi.iloc[-1]
last_day = last_col.index[-1]
plt.figure(figsize=(12, 8))
plt.title('Top 10 countries with highest confirmed cases', fontsize=14)
sns.barplot(x=sorted_grouped_conf[last_day].head(10),            y=sorted_grouped_conf[last_day].index[:10], orient='h')
plt.xlabel('Total cases by '+last_day)
plt.grid()
plt.show()


# ## Exercise 3

# In[12]:


# Total confirmed cases for a given country
def get_total_confirmed_ofcountry(country):
    df_country = confi['Country/Region']==country
    total = confi[df_country].iloc[:, 4: ].apply(sum, axis=0)
    total.index = pd.to_datetime(total.index)
    return total

#polynomial model
def model(x, p1, p2, p3, p4):
    y = p1*np.power(x, 2)+p2*np.power(x,3)+p3*np.power(x,4)+p4*np.power(x,5)
    return y

# Fit the data with polynomial curve
def model_cases_ofcountry(country):
    df = get_total_confirmed_ofcountry(country)
    df = df.reset_index(drop = True)
    pars, cov = curve_fit(f=model, xdata=df.index, ydata=df, p0=[0, 0, 0, 0],                             bounds=(-np.inf, np.inf))
    
    # Standard deviations of the parameters; square roots of the diagonal of the cov matrix
    stdevs = np.sqrt(np.diag(cov))
    pred = model(df.index, *pars)
    plt.figure(figsize=(12, 8))
    plt.title(country.upper()+': Total confirmed cases reported', fontsize=14)
    g1, = plt.plot(df.index, df, 'o', lw=3, label = 'actual conf cases')
    g2, = plt.plot(df.index, pred, color='red', lw=4, label = 'predicted conf cases')
    plt.legend(handles=[g1, g2], loc='upper center')
    plt.grid()
    plt.show()
    return stdevs
country = 'United Kingdom'
model_cases_ofcountry(country)


# In[ ]:




