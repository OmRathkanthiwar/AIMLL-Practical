import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv(("Heart.csv"), index_col=0)

# a) SHAPE OF DATA
print("Shape of Data:", df.shape)

# b) MISSING VALUES
print("\nMissing Values:")
print(df.isnull().sum())

# c) DATA TYPE OF EACH COLUMN
print("\nData Types:")
print(df.dtypes)

# d) NUMBER OF ZEROS
print("\nNumber of Zeros:")
print((df == 0).sum())

# e) MEAN AGE
meanAge = df["Age"].mean()
print("\nMean Age:", round(meanAge, 2))

# f) EXTRACT REQUIRED COLUMNS
selectedData = df[["Age", "Sex", "ChestPain", "RestBP", "Chol"]]

print("\nSelected Data:")
print(selectedData)

# TRAINING AND TESTING DATA
trainData, testData = train_test_split(
    selectedData,
    test_size=0.25,
    random_state=42
)

print("\nTraining Data Shape:", trainData.shape)
print("Testing Data Shape:", testData.shape)

print("\nTraining Data:")
print(trainData)

print("\nTesting Data:")
print(testData)