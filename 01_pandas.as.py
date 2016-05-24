#!/usr/bin/env python

'''
=== GA Data Science Q2 2016 ===

Assignment 1: Introduction to pandas
'''

import os

import numpy as np
import pandas as pd

'''
Exercise 1
'''

# Read in the World Bank World Development Indicators data from `wbwdi.csv`
# into a DataFrame called `wbwdi`
wbdi = pd.read_csv('wbwdi.csv')

# Print the ‘head’ and ‘tail’
print (wbdi.head())
print (wbdi.tail())

# Examine the row names (index), data types, and shape
wbdi.index
wbdi.dtypes
wbdi.shape

# Print the 'LIFEXP' Series
print(wbdi['LIFEXP'])

# Calculate the mean 'LIFEXP' for the entire dataset
wbdi.LIFEXP.mean()

# Count the number of occurrences of each 'Countrygp'
wbdi.Countrygp.value_counts()

# BONUS: Display only the number of rows of `wbwdi`
print(len(wbdi))

# BONUS: Display the 3 most frequent values of 'Countrygp'
print(wbdi.Countrygp.value_counts().sort_values(ascending=False).head(3))
'''
Exercise 2
'''

# Filter `wbwdi` to only include African countries
wbdi[wbdi.Countrygp == 2.0]

# Filter `wbwdi` to only include African countries with LIFEXP > 60
wbdi[(wbdi.Countrygp == 2.0) & (wbdi.LIFEXP > 60)]

# Calculate the mean 'LIFEXP' for all of Africa
wbdi[wbdi.Countrygp == 2.0].LIFEXP.mean()

# Determine which 10 countries have the highest LIFEXP
# For simplicity I am assuming here you only want to see the two relevant columns
wbdi[['Country', 'LIFEXP']].sort_values('LIFEXP', ascending=False).head(10)

# BONUS: Sort `wbwdi` by 'Countrygp' and then by 'LIFEXP' (in a single command)
wbdi.sort_values(['Countrygp', 'LIFEXP'], ascending=[True, False])

# BONUS: Filter `wbwdi` to only include African or Middle Eastern countries
#        without using `|`.
wbdi.query('Countrygp == 2.0 or Countrygp == 4.0')

'''
Exercise 3
'''

# Count the number of missing values in each column of `wbwdi`
wbdi.isnull().sum()

# Show only countries for which 'LIFEXP' is missing
wbdi[wbdi.LIFEXP.isnull()]

# How many rows remain if you drop all rows with any missing values?
len(wbdi.dropna())

# BONUS: Create a new column called 'initial' that contains the first letter of
#        the country name (e.g., 'A' for Afghanistan)
wbdi['initial'] = wbdi.Country.str[0]

'''
Exercise 4
'''

# Calculate the mean 'LIFEXP' by 'Countrygp'
wbdi.groupby('Countrygp').LIFEXP.mean()

# Calculate the minimum and maximum 'LIFEXP' by 'Countrygp'
wbdi.groupby('Countrygp').LIFEXP.min()
wbdi.groupby('Countrygp').LIFEXP.max()

# BONUS: Cross-tabulate 'Countrygp' and 'initial'
pd.crosstab(wbdi.Countrygp, wbdi.initial)

# BONUS: Calculate the median 'LIFEXP' for each combination of 'Countrygp' and
#        'initial'
wbdi.pivot_table(values='LIFEXP', index=['Countrygp', 'initial'], aggfunc='median')
