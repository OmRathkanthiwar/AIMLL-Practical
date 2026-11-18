import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("Social_Network_Ads.csv")

# DATA PREPROCESSING
df = df.drop(columns=["User ID"])
df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

print("Missing Values:")
print(df.isnull().sum())

df = df.dropna()

# INPUT AND OUTPUT
X = df.drop(columns=["Purchased"])
y = df["Purchased"]

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# FEATURE SCALING
scaler = StandardScaler()
XTrain = scaler.fit_transform(XTrain)
XTest = scaler.transform(XTest)

# SVM MODEL
model = SVC()
model.fit(XTrain, yTrain)

# PREDICTION
yPred = model.predict(XTest)

# EVALUATION
print("Accuracy:", accuracy_score(yTest, yPred))
print("\nConfusion Matrix:\n", confusion_matrix(yTest, yPred))
print("\nClassification Report:\n", classification_report(yTest, yPred))

# VISUALIZATION
plt.scatter(yTest, yPred)
plt.xlabel("Actual Purchased")
plt.ylabel("Predicted Purchased")
plt.title("Actual vs Predicted Purchase")
plt.show()
