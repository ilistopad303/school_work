import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#-------------------------
#task 1

#load provided dataset
file_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

#find all string columns
categorical_comlumns = df.select_dtypes(include=['object']).columns

#initialize LabelEncoder and apply label encoding to each categorical column
le = LabelEncoder()
for column in categorical_comlumns:
    df[column] = le.fit_transform(df[column].astype(str))

#-------------------------
#task2

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

#plot elbow curve
plt.figure(figsize=(10,5))
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#----------------------------
#task3
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df)

kmeans_pca = KMeans(n_clusters=3, init='k-means++', random_state=42)
clusters_pca = kmeans_pca.fit_predict(df_pca)

# Create a scatter plot to visualize the clusters
plt.figure(figsize=(10, 7))
plt.scatter(df_pca[:, 0], df_pca[:, 1], c=clusters_pca, cmap='viridis', marker='o')
plt.title('Clusters Visualization with PCA')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster')
plt.show()

#----------------------------
#Task4

df['Cluster'] = clusters_pca

cluster_summary = df.groupby('Cluster').mean()
print(cluster_summary)

#Lab Report
# In this lab we took a dataset and processed it in more depth than we have in the past.
# This included using the elbow method and using Kmeans based on the results of the elbow
# graph. The number of cluster was determined to be three as per the elbow graph.
# by using this we were able to cluster the data into meaningful groupswhich can then be used to create deeper insight
# and support strategic decision making in certain areas such as marketing, customer service, and product developement
# based on these segments.