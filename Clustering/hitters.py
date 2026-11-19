import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# LOAD DATASET
df = pd.read_csv("hitters.csv")

# DATA PREPROCESSING
df.replace("NA", pd.NA, inplace=True)

# HANDLE MISSING VALUES
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# CONVERT CATEGORICAL DATA
df = pd.get_dummies(
    df,
    columns=["League", "Division", "NewLeague"],
    drop_first=True
)

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
plt.xlabel("AtBat")
plt.ylabel("Hits")
plt.title("K-Means Clustering")
plt.show()

# VISUALIZATION - AGGLOMERATIVE
plt.scatter(X[:, 0], X[:, 1], c=labels2)
plt.xlabel("AtBat")
plt.ylabel("Hits")
plt.title("Agglomerative Clustering")
plt.show()
