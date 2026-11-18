import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("loan_prediction.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()
df = df.drop(columns=["Loan_ID"])

# HANDLE MISSING VALUES
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# CONVERT CATEGORICAL DATA
df = pd.get_dummies(
    df,
    columns=["Gender", "Married", "Dependents", "Education",
             "Self_Employed", "Property_Area"],
    drop_first=True
)

# CONVERT TARGET TO 0 OR 1
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

# INPUT AND OUTPUT
X = df.drop(columns=["Loan_Status"])
y = df["Loan_Status"]

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# DECISION TREE MODEL
model = DecisionTreeClassifier(random_state=42)
model.fit(XTrain, yTrain)

# PREDICTION
yPred = model.predict(XTest)

# EVALUATION
print("Accuracy:", accuracy_score(yTest, yPred))
print("\nConfusion Matrix:\n", confusion_matrix(yTest, yPred))
print("\nClassification Report:\n", classification_report(yTest, yPred))

# VISUALIZATION
plt.figure(figsize=(15, 8))
plot_tree(model, feature_names=X.columns,
          class_names=["Rejected", "Approved"], filled=True)
plt.show()
