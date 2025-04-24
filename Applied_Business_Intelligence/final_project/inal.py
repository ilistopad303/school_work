import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data_set = "Historical State Residency per year.csv"
df = pd.read_csv(data_set)

print(df.info())
#Cleanup Data

df.drop(columns=["Average Apportionment Population Per Representative", "Number of Representatives", "Change in Number of Representatives"], axis=1, inplace=True)

# le = LabelEncoder()
# for column in df.select_dtypes(include='object').columns:
#     df[column] = le.fit_transform(df[column])

df.rename(columns={"Name": "State"}, inplace=True)

df.sort_values(by=["State", "Year"], inplace=True, ascending=True)

#Write the new CSV file to use with Power BI
df.to_csv("Cleaned_CSV.csv", index=False)


print(df.info())
print(df.head())

