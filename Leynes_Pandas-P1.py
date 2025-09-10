#!/usr/bin/env python
# coding: utf-8

# ## **Programming Assignment 3** Part 1
# #### Python Data Analysis (Pandas)
# #### This jupyter notebook contains (1) problem that utilizes Pyhton3 - Pandas library
# #### [Github Repository: https://github.com/ramongerix/python-exp3-pandas]
# #### --------------------------------------------------------------------------------------------------------------
# 

# ### **Problem 1**

# In[13]:


# to access Pandas library
import pandas as pd


# #### **(1.a)** Load the cars.csv csv file into a data frame using pandas.

# In[8]:


# read & load the "cars.csv" csv file into a data frame using pandas
cars = pd.read_csv('cars.csv')
cars


# #### **(1.b)** Displays the first five rows of the resulting cars.

# In[10]:


# displays the first five resulting cars
# using variable "cars" followed by a (.) dot "head" to return the first 5 rows of the given/loaded csv data
cars.head()


# In[11]:


# displays the last five resulting cars
# using variable "cars" followed by a (.) dot "tail" to return the last 5 rows of the given/loaded csv data
cars.tail()


# ###

# #### --------------------------------------------------------------------------------------------------------------
# ##### End of Problem 1, to access Problem 2 click this link to be redirected:
# ##### **https://github.com/ramongerix/python-exp3-pandas/blob/main/Leynes_Pandas-P2.py**
