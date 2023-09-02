import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv("test_data.csv", header="infer")
print(data.head())

# Create dataframe
sample_df = pd.DataFrame({
    'id': [1,2,3],
    'Salary': [46000, 58000, 86400]})

# Filtering
filtered_data = data[(data.Temperature >= 20) & (data.Stocks > 100)]
filtered_data = data[(data['Temperature'] >= 20) & (data['Stocks'] > 100)]

# Rename columns
renamed_data = data.rename(columns={"Date": "NewDate", "Temperature": "Kion"})

# Distinct & unique
unique_stocks = data[['Stocks']].drop_duplicates()  # Used for dataframes
unique_stocks = data['Stocks'].unique()  # Used for series
num_unique_stocks = unique_stocks['Stocks'].nunique() # number of unique values

unique_stocks.drop_duplicates(subset='email', keep='first', inplace=True)

# Sorting
sorted_data = data.sort_values(by=['Stocks', 'Temperature'], ascending=False)

# Joins
joined_data = data.merge(data, how="inner", left_on="Date", right_on="Date", suffixes=('_employee', '_dpmt'))
full_df = data.merge(data, on='departmentId', suffixes=('_employee', '_dpmt'))

# Create new column based on condition - loc
data_newCol = data.copy()
data_newCol['new_col'] = 0
data_newCol.loc[data.Texts.str.startswith("S"), 'new_col'] = data_newCol['Sales']

# Group by
grouped_data = data.groupby("date").agg({'stock': "avg"}).reset_index() # Reset index used to retain the group by column

# String operations
short_data = data[data.Texts.str.len() < 3]
string_data = data.copy()
string_data['Texts'] = string_data['Texts'].str.capitalize()
string_data['Texts'] = string_data['Texts'].str.lower()
# regular_expression = r""
# string_data['Texts'] = string_data['Texts'].str.match(regular_expression)
string_data['Texts'] = string_data['Texts'].str.contains("text")


