import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv("test_data.csv", header="infer")
print(data.head())

# Filtering
filtered_data = data[(data.Temperature >= 20) & (data.Stocks > 100)]
filtered_data = data[(data['Temperature'] >= 20) & (data['Stocks'] > 100)]

# Rename columns
renamed_data = data.rename(columns={"Date": "NewDate", "Temperature": "Kion"})

# Distinct & unique
unique_stocks = data[['Stocks']].drop_duplicates()  # Used for dataframes
unique_stocks = data['Stocks'].unique()  # Used for series

# Sorting
sorted_data = data.sort_values(by=['Stocks', 'Temperature'], ascending=False)

# Joins
joined_data = data.merge(data, how="inner", left_on="Date", right_on="Date")

# Create new column based on condition - loc
data_newCol = data.copy()
data_newCol['new_col'] = 0
data_newCol.loc[data.Texts.str.startswith("S"), 'new_col'] = data_newCol['Sales']

# String operations
short_data = data[data.Texts.str.len() < 3]
string_data = data.copy()
string_data['Texts'] = string_data['Texts'].str.capitalize()
string_data['Texts'] = string_data['Texts'].str.lower()

