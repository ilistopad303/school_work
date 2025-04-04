import pandas as pd
from sklearn.preprocessing import LabelEncoder

#dataset 1
customers_df = pd.read_csv('global_superstore_data/customers.csv')
print("-----------------------------------------------------")
print(customers_df.head())
print("\n")
print(customers_df.describe())
print("\n")
print(customers_df.info())

#dataset 2
orders_df = pd.read_csv('global_superstore_data/orders.csv')
print("-----------------------------------------------------")
print(orders_df.head())
print("\n")
print(orders_df.describe())
print("\n")
print(orders_df.info())

#dataset 3
products_df = pd.read_csv('global_superstore_data/products.csv')
print("-----------------------------------------------------")
print(products_df.head())
print("\n")
print(products_df.describe())
print("\n")
print(products_df.info())

#merge products and orders
products_orders_df = pd.merge(products_df, orders_df, on='Product ID')

#join customer information
products_orders_customers_df = customers_df.set_index('Customer ID').join(products_orders_df.set_index('Customer ID'))

#concat tables
concat_df = pd.concat([customers_df, products_df, orders_df], join='inner', axis=1, ignore_index=False)

#Check for conistency and possible cleanup items needed
print("\nChecking for missing values in merged_df:")
print(products_orders_df.isnull().sum())

print("\nChecking for duplicate rows in merged_df:")
print(products_orders_df.duplicated().sum())

print("\nChecking for missing values in joined_df:")
print(products_orders_customers_df.isnull().sum())

print("\nChecking for duplicate rows in joined_df:")
print(products_orders_customers_df.duplicated().sum())

print("\nChecking for missing values in concat_df:")
print(concat_df.isnull().sum())

print("\nChecking for duplicate rows in concat_df:")
print(concat_df.duplicated().sum())

#Lab Review
#
# The data that was derived from the provided Datasets helps us gain an insight into the superstores sales and customer orders,
# especially when combining the datasheets all into one. That gives a complete look and overview of the sales/orders.
# Now the Data does have some postal code entries that are missing. Depending on the analytics, With the amount that are missing
# I wouldn’t want to just delete those rows. Instead, I would probably either write a script to take the city and insert the correct
# postal code. Now if postal code is not important, say you could just use the city or state instead, that would be the easiest and then
# those missing postal codes are a null point.
# 
# This lab was  a good one and taught me a lot about the inner workings of pandas and data frames within python. I liked that it walked
# me through and helped me understand the difference and how to use the different ways of combining datasets. Along with that it made me
# think of different ways to deal with missing data rather than just dropping it, because as I mentioned above depending on the analytics
# you wouldn’t want to drop really any in a set like this, but let alone some 40000 rows.
