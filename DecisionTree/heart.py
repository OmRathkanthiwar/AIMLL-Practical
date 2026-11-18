import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("Heart.csv", index_col=0)

# DATA PREPROCESSING
df.columns = df.columns.str.strip()
df.replace("?", pd.NA, inplace=True)

# HANDLE MISSING VALUES
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# CONVERT CATEGORICAL DATA
df = pd.get_dummies(
    df,
    columns=["ChestPain", "Thal"],
    drop_first=True
)

# CONVERT TARGET TO 0 OR 1
df["AHD"] = df["AHD"].map({"Yes": 1, "No": 0})

# INPUT AND OUTPUT
X = df.drop(columns=["AHD"])
y = df["AHD"]

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
plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No Disease", "Heart Disease"],
    filled=True
)
plt.show()
