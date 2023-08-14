import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv("test_data.csv", header="infer")
# print(data.head())


# Filtering
filtered_data = data[(data.Temperature >= 20) & (data.Stocks > 100)]
filtered_data = data[(data['Temperature'] >= 20) & (data['Stocks'] > 100)]
print(filtered_data.head())