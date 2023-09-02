import pandas as pd

# Create the Customers DataFrame
customers_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Joe', 'Henry', 'Sam', 'Max', 'Alice', 'Bob', 'Charlie', 'David']
}
customers = pd.DataFrame(customers_data)

# Create the Orders DataFrame
orders_data = {
    'id': [1, 2, 3, 4, 5],
    'customerId': [3, 1, 2, 6, 4]
}
orders = pd.DataFrame(orders_data)

# Display the Customers and Orders DataFrames
print(customers)
print(orders)


# SOLUTION 1
out = customers[~customers.id.isin(orders.customerId)][['name']]
out = out.rename(columns={"name": "Customers"})
# out.columns = ['Customers']
print(out)

# SOLUTION 2
out = customers.merge(orders['customerId'], how='left', left_on="id", right_on='customerId')
out = out[out.customerId.isna()][['name']]
out = out.rename(columns={"name": "Customers"})
print(out)
