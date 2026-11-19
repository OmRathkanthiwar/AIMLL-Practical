
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# LOAD DATASET
df = pd.read_csv("Cities_r2.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()

df = df.drop(columns=[
    "name_of_city", "state_code", "state_name",
    "dist_code", "location"
])

df = df.dropna()

# FEATURE SCALING
scaler = StandardScaler()
X = scaler.fit_transform(df)

# K-MEANS CLUSTERING
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeansLabels = kmeans.fit_predict(X)

print("K-Means Clustering:")
print("Cluster Labels:", kmeansLabels)
print("Silhouette Score:", silhouette_score(X, kmeansLabels))

# AGGLOMERATIVE CLUSTERING
agg = AgglomerativeClustering(n_clusters=3)
aggLabels = agg.fit_predict(X)

print("\nAgglomerative Clustering:")
print("Cluster Labels:", aggLabels)
print("Silhouette Score:", silhouette_score(X, aggLabels))

# VISUALIZATION USING PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeansLabels, cmap="viridis")
plt.title("K-Means Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=aggLabels, cmap="viridis")
plt.title("Agglomerative Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()
plt.show()
