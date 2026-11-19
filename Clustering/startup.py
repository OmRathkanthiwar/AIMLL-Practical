
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# LOAD DATASET
df = pd.read_csv("50_Startups.csv")

# DATA PREPROCESSING
df = pd.get_dummies(df, columns=["State"], drop_first=True)
df = df.dropna()

# FEATURE SCALING
scaler = StandardScaler()
X = scaler.fit_transform(df)

# K-MEANS CLUSTERING
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels1 = kmeans.fit_predict(X)

print("K-Means Clustering:")
print("Cluster Labels:", labels1)
print("Silhouette Score:", silhouette_score(X, labels1))

# AGGLOMERATIVE CLUSTERING
agg = AgglomerativeClustering(n_clusters=3)
labels2 = agg.fit_predict(X)

print("\nAgglomerative Clustering:")
print("Cluster Labels:", labels2)
print("Silhouette Score:", silhouette_score(X, labels2))

# VISUALIZATION - K-MEANS
plt.scatter(X[:, 0], X[:, 1], c=labels1)
plt.xlabel("R&D Spend")
plt.ylabel("Administration")
plt.title("K-Means Clustering")
plt.show()

# VISUALIZATION - AGGLOMERATIVE
plt.scatter(X[:, 0], X[:, 1], c=labels2)
plt.xlabel("R&D Spend")
plt.ylabel("Administration")
plt.title("Agglomerative Clustering")
plt.show()
