import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Import and create Dataframe
data_path = 'WA_IT-Help-Desk_flaws.csv'
df = pd.read_csv(data_path)

#Inspect the Dataframe
print("\nFirst 5 rows of dataset:")
print(df.head())

print("\nInfo about dataset:")
print(df.info())

print("\nStatistical summary of dataset:")
print(df.describe())

#Identify quality issues
print("\nChecking for missing values:")
print(df.isnull().sum())

print("\nChecking for Duplicate Rows:")
print(df.duplicated().sum())

#data Cleaning
print("\nCleaning up Data")
#drop missing
print("Dropping rows with null values")
df.dropna(inplace= True)

#remove duplicates
print("Removing duplicate rows")
df.drop_duplicates(inplace=True)

#correct inconsistencies/standardize categorical data entries
print("Correcting inconsistencies via encoding")
encoder = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = encoder.fit_transform(df[col])

# Data Validation
print("\nData After Cleaning")
print(df.head())
print(df.info())

print("\nChecking for duplicate rows:")
print(df.duplicated().sum())

