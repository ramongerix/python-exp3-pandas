#!/usr/bin/env python
# coding: utf-8

# ## **Programming Assignment 3** Part 2
# #### Python Data Analysis (Pandas)
# #### This jupyter notebook contains (1) problem that utilizes Pyhton3 - Pandas library
# #### [Github Repository: https://github.com/ramongerix/python-exp3-pandas]
# #### --------------------------------------------------------------------------------------------------------------
# 

# ### **Problem 2**

# In[1]:


# to access Pandas library
import pandas as pd


# In[3]:


# Load the cars.csv csv file into a data frame using pandas.
cars = pd.read_csv('cars.csv')
cars


# ##### Utilizing the dataframe provided in Problem 1, this problem will extract the following information through a combination of subsetting, slicing, and indexing operations.
# #### **(2.a)** Display the first five rows with odd-numbered (columns 1, 3, 5, 7...) of cars.

# In[5]:


# Show first 5 rows of 'cars' and select odd columns (1,3,5,7) using iloc slicing.
cars.iloc[:5, 1::2]
cars


# #### **(2.b)** Display the row that contains the ‘Model’ of ‘Mazda RX4

# In[8]:


# using ".head" will display a more concise and minimal output by using datframe ui. 
cars.head(1)


# #### **(2.c)** How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[10]:


# select row 23, column 2 from cars
cars.iloc[[23],[2]]


# #### **(2.d)** Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[13]:


# select rows 1, 28, 18 and columns 0, 2, 10 from cars
cars.iloc[[1,28,18],[0, 2, 10]]


# ###

# ##### --------------------------------------------------------------------------------------------------------------
# ##### End of Problem 2, to access Problem 1 click this link to be redirected:
# ##### **https://github.com/ramongerix/python-exp3-pandas/blob/main/Leynes_Pandas-P1.py**
