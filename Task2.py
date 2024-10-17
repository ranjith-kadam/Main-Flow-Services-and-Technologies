#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[3]:


import pandas as pd

# Read a CSV file
df = pd.read_csv(r'D:\RANJITH\PYTHON PROGRAMMING\Main Flow Technologies\A,B,C,D.csv')

# Display the first few rows of the DataFrame
print(df.head())


# In[4]:


# Removing rows with any missing values
df_cleaned = df.dropna()

# Display the cleaned DataFrame
print(df_cleaned)


# In[5]:


# Fill missing values with a specific value
df_filled = df.fillna(0)

# Display the DataFrame with filled values
print(df_filled)


# In[6]:


# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Display the DataFrame without duplicates
print(df_no_duplicates)


# In[7]:


# Filtering data
# Filter rows where column 'A' > 10
filtered_df = df[df['A'] > 10]

# Display the filtered DataFrame
print(filtered_df)


# In[8]:


# Sorting data

sorted_df = df.sort_values(by='B')

# Display the sorted DataFrame
print(sorted_df)


# In[9]:


# Grouping Data
grouped_df = df.groupby('C')['D'].mean()

# Display the grouped DataFrame
print(grouped_df)


# In[ ]:





# In[ ]:




