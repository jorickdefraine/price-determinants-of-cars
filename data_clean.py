#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("final_Cars_DB.csv", index_col=0)

# shape and data types of the data
print(df.shape)
print(df.dtypes)

# df.dtypes.value_counts()
# df.isnull().sum().sum()

to_Null = ['Nombre_de_porte', 'Nombre_de_place', 'department', 'number_photos', 'number_options', 'covid_seller',
           'number_ads_seller']
to_Null_ind = [7, 8, 15, 17, 18, 21, 23]
for col in to_Null_ind:
    for i in range(len(df)):
        try:
            isinstance(int(df.iloc[i, col]), int) == True
        except ValueError:
            print("Not a float")
            df.iloc[i, col] = np.NaN

# df.isnull().sum().sum()/len(df)
print("start extract")
extr = df['year_seller'].str.extract(r'^(\d{4})', expand=False)
print("end extract")
df['year_seller'] = pd.to_numeric(extr)
df['year_seller'].dtype

# df.isnull().values.any()

for column in df.columns:
    print(column)
    df[column].fillna(method='ffill', inplace=True)

# df.isnull().sum().sum()

df.to_csv('CLEAN_final_cars_DB.csv', mode='w')