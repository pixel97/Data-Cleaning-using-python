#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\My Projects\Data-Cleaning-using-python\bhp.csv")

data.head()

plt.hist(data.price_per_sqft, bins=20, rwidth=0.8)
plt.xlabel('Price per square ft')
plt.ylabel('Count')
plt.yscale('log')
plt.show()

data.price_per_sqft.describe()


min_threshold,max_threshold = data.price_per_sqft.quantile([0.001,0.999])
min_threshold,max_threshold 

#Using standard deviation to remove outliers


data_outliers = data[(data.price_per_sqft>min_threshold) & (data.price_per_sqft<max_threshold)]
data_outliers.shape

upper_limit = data_outliers.price_per_sqft.mean() + 4*data_outliers.price_per_sqft.std()
upper_limit

lower_limit = data_outliers.price_per_sqft.mean() - 4*data_outliers.price_per_sqft.std()
lower_limit

data_outliers1 = data_outliers[(data_outliers.price_per_sqft>lower_limit) & (data_outliers.price_per_sqft<upper_limit)]
data_outliers1.shape


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (12,8)


plt.hist(data_outliers1.price_per_sqft,bins=20,rwidth=0.8)
plt.xlabel('Price_per_sqft')
plt.ylabel('Count')
plt.show()

from scipy.stats import norm
plt.hist(data_outliers1.price_per_sqft, bins=20, rwidth=0.8, density=True)
plt.xlabel('Price_per_sqft')
plt.ylabel('Count')

rng = np.arange(-5000, data_outliers1.price_per_sqft.max(), 100)
plt.plot(rng, norm.pdf(rng,data_outliers1.price_per_sqft.mean(),data_outliers1.price_per_sqft.std()))

# Using Z-score to remove outliers

data_outliers['zscore'] = (data_outliers.price_per_sqft - data_outliers.price_per_sqft.mean())/data_outliers.price_per_sqft.std()
data_outliers.head()


new_data = data_outliers1[(data_outliers.zscore>-4) & (data_outliers.zscore<4)]
new_data.shape

