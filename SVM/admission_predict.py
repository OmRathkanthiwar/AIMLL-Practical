
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("Admission_Predict.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()
df = df.drop(columns=["Serial No."])

# CONVERT ADMISSION CHANCE TO 0 OR 1
col = "Chance of Admit"
df["Admitted"] = (df[col] >= 0.5).astype(int)

# INPUT AND OUTPUT
X = df.drop(columns=[col, "Admitted"])
y = df["Admitted"]

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
plt.xlabel("Actual Admission")
plt.ylabel("Predicted Admission")
plt.title("Actual vs Predicted Admission")
plt.show()
