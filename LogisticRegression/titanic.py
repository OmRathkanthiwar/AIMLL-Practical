import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# LOAD DATASET

df = pd.read_csv("Titanic-Dataset.csv")


# SELECT FEATURES

data = df[[
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked",
    "Survived"
]]

# HANDLE MISSING VALUES

data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# CONVERT CATEGORICAL DATA

data = pd.get_dummies(
    data,
    columns=["Sex", "Embarked"],
    drop_first=True
)

# INPUT AND OUTPUT

X = data.drop("Survived", axis=1)
y = data["Survived"]

# TRAIN TEST SPLIT

XTrain, XTest, yTrain, yTest = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# LOGISTIC REGRESSION

model = LogisticRegression(max_iter=1000)

model.fit(XTrain, yTrain)

# PREDICTION

yPred = model.predict(XTest)

# PERFORMANCE

accuracy = accuracy_score(yTest, yPred)
precision = precision_score(yTest, yPred)
recall = recall_score(yTest, yPred)

print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))

# VISUALIZATION

plt.scatter(
    df["Age"],
    df["Survived"]
)

plt.xlabel("Age")
plt.ylabel("Survived")
plt.title("Titanic Survival")

plt.show()