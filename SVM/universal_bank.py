import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("UniversalBank.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()
df = df.drop(columns=["ID", "ZIP Code"])

print("Missing Values:")
print(df.isnull().sum())

df = df.dropna()

# INPUT AND OUTPUT
X = df.drop(columns=["Personal Loan"])
y = df["Personal Loan"]

# FEATURE SCALING
scaler = StandardScaler()
X = scaler.fit_transform(X)

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# SVM MODEL
model = SVC()
model.fit(XTrain, yTrain)

# PREDICTION
yPred = model.predict(XTest)

# EVALUATION
print("\nAccuracy:", accuracy_score(yTest, yPred))
print("\nConfusion Matrix:\n", confusion_matrix(yTest, yPred))
print("\nClassification Report:\n", classification_report(yTest, yPred))

# VISUALIZATION
plt.scatter(yTest, yPred)
plt.xlabel("Actual Personal Loan")
plt.ylabel("Predicted Personal Loan")
plt.title("Actual vs Predicted")
plt.show()
