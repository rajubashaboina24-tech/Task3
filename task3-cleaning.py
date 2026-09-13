#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[17]:


df = pd.read_csv("C:\\Users\\Welcome\\Downloads\\10,000 records healthcare data.csv")
df.head()


# In[19]:


missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum()
})

display(missing)


# In[21]:


if missing["Missing Values"].sum() == 0:
    print("Completeness: PASS")
else:
    print("Completeness: FAIL")


# In[39]:


duplicate_names = df[df["Name"].duplicated()]

display(duplicate_names)


# In[35]:


duplicate_names = df[""].duplicated().sum()

print("Duplicate names:", duplicate_names)

if duplicate_names.sum() == 0:
    print("Duplicates: PASS")
else:
    print("Duplicates: FAIL")

