import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Set the random seed for reproducibility
np.random.seed(42)

# Create date range for the Date column
date_range = pd.date_range(start='2023-01-01', periods=200, freq='D')

# Create a dictionary with 10 columns of meaningful data
data = {
    'Date': date_range,
    'Temperature': np.random.uniform(15, 30, 200),  # Temperature in Celsius
    'Humidity': np.random.uniform(40, 80, 200),     # Humidity in percentage
    'Pressure': np.random.uniform(980, 1050, 200),  # Pressure in hPa
    'WindSpeed': np.random.uniform(0, 20, 200),     # Wind speed in km/h
    'Rainfall': np.random.uniform(0, 10, 200),      # Rainfall in mm
    'Sales': np.random.randint(100, 1000, 200),     # Sales amount
    'Stocks': np.random.randint(0, 1000, 200),      # Stock quantities
    'Distance': np.random.uniform(10, 200, 200),    # Distance in km
    'Duration': np.random.randint(5, 120, 200),      # Duration in minutes
    'Texts': ["Sample_text" for i in range(200)]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

df.to_csv("test_data.csv", header=True, index=False)




