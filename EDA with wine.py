#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv("https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv")


# In[4]:


df.head()


# In[5]:


df.info()## to get the summary of data set


# In[6]:


## descriptive summary of dataset
df.describe()


# In[7]:


## shape of dataset
df.shape


# In[8]:


### list down all dataset
df.columns


# In[10]:


df['Alcohol'].unique()


# In[11]:


df['Alcohol'].value_counts()


# In[12]:


## missing values
df.isnull().sum()


# In[15]:


## to check duplicate words
df.duplicated()


# In[17]:


## remove duplicate records
df.drop_duplicates(inplace=True)


# In[18]:


df.corr()


# In[19]:


import matplotlib.pyplot as plt


# In[21]:


import seaborn as sns
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True)


# In[23]:


## categorical plot
sns.catplot(x='Alcohol',y='Ash',data=df,kind='box')


# In[ ]:




