#!/usr/bin/env python
# coding: utf-8

import pandas as pd


data = pd.read_csv(r"C:\My Projects\Data-Cleaning-using-python\AB_NYC_2019.csv")
data.head()


data['price_per_night'] = data['price']/data['minimum_nights']
data.head()

data.describe()


min_threshold,max_threshold = data.price.quantile([0.01,0.999])
min_threshold,max_threshold


data[data.price<min_threshold]

data[data.price>max_threshold]

clean_data = data[(min_threshold<data.price) & (data.price<max_threshold)]
clean_data.shape

clean_data.price.describe()




