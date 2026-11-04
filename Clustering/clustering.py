import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# LOAD DATASET
df = pd.read_csv("Mall_Customers.csv")

print(df.head())
print(df.isnull().sum())

# DATA PREPROCESSING
df = pd.get_dummies(df, columns=["Genre"], drop_first=True, dtype=int)

X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# K-MEANS CLUSTERING
model1 = KMeans(n_clusters=5, random_state=42, n_init=10)
labels1 = model1.fit_predict(X)

print("K-Means Silhouette Score:", silhouette_score(X, labels1))

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels1)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clustering")
plt.show()

# FIND HIGHEST-SPENDING K-MEANS CLUSTER
df["KMeans_Cluster"] = labels1

kmeansAvg = df.groupby("KMeans_Cluster")["Spending Score (1-100)"].mean()
kmeansBest = kmeansAvg.idxmax()

print("\nK-Means Average Spending Scores:")
print(kmeansAvg.round(2))
print("Highest-Spending Cluster:", kmeansBest)
print("Average Spending Score:", round(kmeansAvg.max(), 2))

# HIERARCHICAL CLUSTERING
model2 = AgglomerativeClustering(n_clusters=5, linkage="ward")
labels2 = model2.fit_predict(X)

print("\nHierarchical Silhouette Score:", silhouette_score(X, labels2))

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels2)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Hierarchical Clustering")
plt.show()

# FIND HIGHEST-SPENDING HIERARCHICAL CLUSTER
df["Hierarchical_Cluster"] = labels2

hierAvg = df.groupby("Hierarchical_Cluster")["Spending Score (1-100)"].mean()
hierBest = hierAvg.idxmax()

print("\nHierarchical Average Spending Scores:")
print(hierAvg.round(2))
print("Highest-Spending Cluster:", hierBest)
print("Average Spending Score:", round(hierAvg.max(), 2))
