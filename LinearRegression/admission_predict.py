import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# LOAD DATASET
df = pd.read_csv("Admission_Predict.csv", index_col=0)

# DATA PREPROCESSING
df.columns = df.columns.str.strip()

print("Missing Values:")
print(df.isnull().sum())

df = df.dropna()

# INPUT AND OUTPUT
X = df[[
    "GRE Score",
    "TOEFL Score",
    "University Rating",
    "SOP",
    "LOR",
    "CGPA",
    "Research"
]]

y = df["Chance of Admit"]

# TRAIN-TEST SPLIT
XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# LINEAR REGRESSION
model = LinearRegression()
model.fit(XTrain, yTrain)

# PREDICTION
yPred = model.predict(XTest)

# EVALUATION
mse = mean_squared_error(yTest, yPred)
mae = mean_absolute_error(yTest, yPred)
r2 = r2_score(yTest, yPred)

print("\nMean Squared Error:", round(mse, 2))
print("Mean Absolute Error:", round(mae, 2))
print("R-Square:", round(r2, 2))

# VISUALIZATION
plt.scatter(yTest, yPred)
plt.xlabel("Actual Chance of Admit")
plt.ylabel("Predicted Chance of Admit")
plt.title("Actual vs Predicted Chance of Admit")
plt.show()
