
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("UniversalBank.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()

print("Missing Values:")
print(df.isnull().sum())

df = df.dropna()

# INPUT AND OUTPUT
X = df.drop(["ID", "ZIP Code", "Personal Loan"], axis=1)
y = df["Personal Loan"]

# FEATURE SCALING
scaler = StandardScaler()
X = scaler.fit_transform(X)

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# LOGISTIC REGRESSION
model = LogisticRegression(max_iter=1000)
model.fit(XTrain, yTrain)

# PREDICTION
yPred = model.predict(XTest)

# EVALUATION
accuracy = accuracy_score(yTest, yPred)
cm = confusion_matrix(yTest, yPred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(yTest, yPred))

# VISUALIZATION
plt.scatter(yTest, yPred)
plt.xlabel("Actual Personal Loan")
plt.ylabel("Predicted Personal Loan")
plt.title("Actual vs Predicted")
plt.show()
