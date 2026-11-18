import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_csv("Heart.csv", index_col=0)

# DATA PREPROCESSING
df.replace("?", pd.NA, inplace=True)

# HANDLE MISSING VALUES
for col in df.columns:

    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())


# EXPLORATORY DATA ANALYSIS

# a) SHAPE OF DATA
print("Shape of Data:", df.shape)

# b) MISSING VALUES
print("\nMissing Values:")
print(df.isnull().sum())

# c) DATA TYPES
print("\nData Types:")
print(df.dtypes)

# d) NUMBER OF ZEROS
print("\nNumber of Zeros:")
print((df == 0).sum())

# e) SUMMARY STATISTICS
print("\nSummary Statistics:")
print(df.describe())

# # f) MEAN AGE
# meanAge = df["Age"].mean()
# print("\nMean Age:", round(meanAge, 2))

# g) EXTRACT REQUIRED COLUMNS
selectedData = df[["Age", "Sex", "ChestPain", "RestBP", "Chol"]]

print("\nSelected Data:")
print(selectedData)

# VISUALIZATION
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()
