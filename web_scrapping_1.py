#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[4]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[5]:


soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[6]:


# Get the title
title = soup.title
print(title)


# In[7]:


# Printing the text
text = soup.get_text()
#print(soup.text)


# In[8]:


soup.find_all('a')


# In[9]:


all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# In[10]:


# Print the first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])


# In[11]:


for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)


# In[12]:


str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


# In[13]:


import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)


# In[14]:


df = pd.DataFrame(list_rows)
df.head(10)


# In[15]:


# Data Manipulation and Cleaning
df1 = df[0].str.split(',', expand=True)
df1.head(10)


# In[16]:


df1[0] = df1[0].str.strip('[')
df1.head(10)


# In[17]:


col_labels = soup.find_all('th')


# In[18]:


all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)


# In[19]:


# Converting list of headers into pandas dataframe
df2 = pd.DataFrame(all_header)
df2.head()


# In[20]:


df3 = df2[0].str.split(',', expand=True)
df3.head()


# In[21]:


frames = [df3, df1]
df4 = pd.concat(frames)
df4.head(10)


# In[22]:


# Assigning first row to table header
df5 = df4.rename(columns=df4.iloc[0])
df5.head()


# In[23]:


df5.info()
df5.shape


# In[24]:


df6 = df5.dropna(axis=0, how='any')


# In[25]:


df7 = df6.drop(df6.index[0])
df7.head()


# In[26]:


df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.head()


# In[27]:


df7['Team'] = df7['Team'].str.strip(']')
df7.head()


# In[ ]:





# In[ ]:





# In[ ]:




