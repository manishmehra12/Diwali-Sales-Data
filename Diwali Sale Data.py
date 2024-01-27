#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df =pd.read_csv("Diwali Sales Data.csv", encoding='unicode_escape')
# To avoid encoding error, use 'unicode_escape'


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


# Drop unrelated/blank coloumns (delete option)
df.drop(["Status","unnamed1"],axis=1,inplace=True)


# In[7]:


#check for null values 
pd.isnull(df).sum()


# In[8]:


#drop null values.
# inplace=True is use for saving drop values.
df.dropna(inplace=True)


# In[9]:


pd.isnull(df).sum()


# In[10]:


#change data types (dtypes)
df['Amount'].dtypes


# In[11]:


df['Amount']=df['Amount'].astype('int')


# In[12]:


df['Amount'].dtypes


# In[13]:


df.head(20)


# In[14]:


import matplotlib.pyplot as plot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df.hist(figsize=(20,20))
plot.show()


# In[16]:


pd.crosstab(df['Gender'],df['Age Group'])


# In[17]:


import seaborn as sns


# In[18]:


ax = sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[19]:


Gender_sales = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender',y='Amount', data=Gender_sales)


# In[20]:


Gender_sales = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender',y='Amount', data=Gender_sales)


# In[21]:


#From above graphs we can see that most of the buyers are the females and even the purshaing power of the females are greater then men


# In[22]:


# For checking which "Age Group" shops more than other groups.
sns.countplot(x='Age Group',data=df)


# In[23]:


sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
# "hue" work is show division of men and women.
# for checking which gender shops more.


# In[24]:


# Total Amount vs Age groups
sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group',y= 'Amount', data=sales_age)


# **From above graph we can see that most of the buyers are age groups between 26-35 years female**

# In[26]:


#state
# total number of orders from top 10 states.
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,7)})
sns.barplot(data = sales_state, x='State',y='Orders')


# **From above graphs we see that unexpectedly most of the orders are from the uttar pradesh, maharashtra and karnatka respectively but total sales/amount is from UP, karnataka and maharastra.**

# # **Marital status**

# In[27]:


sns.countplot(x='Marital_Status',data=df)


# In[28]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x='Marital_Status',y='Amount',hue='Gender')


# **From above graph we can that most of the buyers are married (women) and they have heigh purchasing power.**

# # Occupation

# In[41]:


sns.set(rc={'figure.figsize':(20,5)})
sns.countplot(data=df,x='Occupation')


# In[29]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')


# **From above graphs we can see that most of the buyers are working in IT,Aviation and healthcare sector.**

# # Product heading

# In[30]:


sns.set(rc={'figure.figsize':(25,5)})
sns.countplot(data = df, x = 'Product_Category')


# In[31]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(40,10)})
sns.barplot(data = sales_state, x = 'Product_Category',y='Amount')


# **From above graph we can see that most of the sold product are from Food,Footwear and Electronics category.**

# In[56]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')


# # Conclusion

# 
# 
# 
# **Married women age group 26-35 years from UP, Maharashtra and Karnataka working in IT, Healthcare and Adviation are more likely 
# to buy products from Food, Clothing and Electronics category.**
# 
# 
# 
# Thank you!!
