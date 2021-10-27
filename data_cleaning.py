import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

df.drop(['Unnamed: 0', 'Unnamed: 6', 'Name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Luminosity'], axis = 1, inplace = True)
print(df.shape)

df = df.dropna()
print(df.shape)

df.reset_index(drop = True, inplace = True)
print(df.shape)

df.to_csv('final_data.csv')
print(df.info())

print(df.describe())
print(df.head(5))
print(df.dtypes)
print(list(df))