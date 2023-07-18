#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("coviddata.csv")


# In[3]:


data


# In[4]:


data.count()


# In[6]:


data.isnull()


# In[7]:


data.isnull().sum()


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:



sns.heatmap(data.isnull())
plt.show()


# In[12]:


data.head()


# In[14]:


data.groupby('Region').sum().head(20)


# In[19]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# In[20]:


data.Confirmed <10


# In[21]:


data.head()


# In[24]:


data = data[(~data.Confirmed<10)]


# In[25]:


data


# In[26]:


data = pd.read_csv("coviddata.csv")


# In[27]:


data


# In[30]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False)


# In[31]:


data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# In[32]:


data.Region == 'India'


# In[33]:


data.Region == 'Yemen'


# In[35]:


data.sort_values(by = ['Confirmed'] , ascending = True)


# In[36]:


data.sort_values(by = ['Recovered'] , ascending = True)


# In[ ]:




