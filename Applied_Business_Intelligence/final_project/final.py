import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px

year_start = int(input("Please input the start year you'd like to see data for:"))
year_end = int(input("Please input the end year you'd like to see data for:"))




data_set = "Historical State Residency per year.csv"
df = pd.read_csv(data_set)
int_columns = ["Resident Population", "Resident Population"]
#Cleanup Data

df.drop(columns=["Average Apportionment Population Per Representative", "Number of Representatives", "Change in Number of Representatives"], axis=1, inplace=True)


df.rename(columns={"Name": "State"}, inplace=True)

df.sort_values(by=["State", "Year"], inplace=True, ascending=True)

for col in int_columns:
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace(",", "")
    df[col] = df[col].astype('int64')

# Write the new CSV file to use with Power BI
df.to_csv("Cleaned_CSV.csv", index=False)




# Create a line graph of population per state per year
fig = px.line(df, x="Year", y="Resident Population", color="State",
              title="Resident Population",
              labels={"Resident Population": "Population", "Year": "Year", "State": "State"})

fig.update_layout(yaxis=dict(fixedrange=False))
# Find Largest change in population overall
# Filter for years 1910 and 2020
df_filtered = df[df["Year"].isin([year_start, year_end])]
# Pivot the data so we have one row per state and columns for each year
df_pivot = df_filtered.pivot(index="State", columns="Year", values="Resident Population").reset_index()
# Calculate percent change from 1910 to 2020
df_pivot["Percent Change"] = ((df_pivot[year_end] - df_pivot[year_start]) / df_pivot[year_start]) * 100

df_pivot = df_pivot.sort_values(by="Percent Change", ascending=False)

# Print or save result
print(df_pivot[["State", "Percent Change"]])

fig.show()