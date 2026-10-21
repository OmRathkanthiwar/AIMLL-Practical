import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# LOAD DATASET
df = pd.read_csv("train.csv")

# INPUT AND OUTPUT
X = df.drop("price_range", axis=1)
y = df["price_range"]

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# FEATURE SCALING
scaler = StandardScaler()
XTrain = scaler.fit_transform(XTrain)
XTest = scaler.transform(XTest)

# SVM MODEL
model = SVC(kernel="linear")
model.fit(XTrain, yTrain)

# PREDICTION AND EVALUATION
yPred = model.predict(XTest)
print("Accuracy:", accuracy_score(yTest, yPred))
print("Confusion Matrix:\n", confusion_matrix(yTest, yPred))
print("Classification Report:\n", classification_report(yTest, yPred))

# TAKE USER INPUT
print("\nEnter mobile specifications:")
features = []

for col in X.columns:
    features.append(float(input("Enter " + col + ": ")))

# PREDICT PRICE RANGE
phone = pd.DataFrame([features], columns=X.columns)
phone = scaler.transform(phone)
prediction = model.predict(phone)

print("Predicted Price Range:", prediction[0])