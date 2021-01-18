#!/usr/bin/env python
# coding: utf-8

# In[26]:


#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df=pd.read_csv("final_Cars_DB.csv",index_col=0)

# shape and data types of the data
print(df.shape)
print(df.dtypes)

for column in df.columns :
    df[column] = df[column].str.replace('\n', '')

#df.dtypes.value_counts()
#df.isnull().sum().sum()

to_Null= ['Nombre_de_porte','Nombre_de_place','department','number_photos','number_options','covid_seller','number_ads_seller']
to_Null_ind = [7,8,15,17,18,21,23]
for col in to_Null_ind:
    for i in range(len(df)) :
        try:
            isinstance(int(df.iloc[i,col]),int)==True
        except ValueError:
            print("Not an integer")
            df.iloc[i,col]=np.NaN

#df.isnull().sum().sum()/len(df)

extr = df['year_seller'].str.extract(r'^(\d{4})', expand=False)
df['year_seller'] = pd.to_numeric(extr)
df['year_seller'].dtype

#df.isnull().values.any()

for column in df.columns :
    df[column].fillna(method='ffill',inplace=True)
for column in to_Null :
    df[column]=df[column].astype('int64')

#df.isnull().sum().sum()

#df.dtypes




