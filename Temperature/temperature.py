import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# LOAD DATASET

df = pd.read_csv("temperatures.csv")

# INPUT FEATURE

X = df[["YEAR"]]

# USER INPUT

year = int(input("Enter year for temperature prediction: "))

inputYear = pd.DataFrame({"YEAR": [year]})

# MONTHS

months = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
]

# LINEAR REGRESSION

for month in months:

    y = df[month]

    XTrain, XTest, yTrain, yTest = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    model = LinearRegression()

    model.fit(XTrain, yTrain)

    yPred = model.predict(XTest)

    prediction = model.predict(inputYear)

    mse = mean_squared_error(yTest, yPred)
    mae = mean_absolute_error(yTest, yPred)
    r2 = r2_score(yTest, yPred)

    print("\n", month)

    print("Predicted Temperature:", round(prediction[0], 2))
    print("MSE:", round(mse, 2))
    print("MAE:", round(mae, 2))
    print("R-Square:", round(r2, 2))

# VISUALIZATION USING ANNUAL TEMPERATURE

yAnnual = df["ANNUAL"]

XTrain, XTest, yTrain, yTest = train_test_split(
    X,
    yAnnual,
    test_size=0.25,
    random_state=42
)

annualModel = LinearRegression()

annualModel.fit(XTrain, yTrain)

plt.scatter(X, yAnnual)

plt.plot(X, annualModel.predict(X))

plt.xlabel("Year")
plt.ylabel("Annual Average Temperature")
plt.title("Linear Regression - Annual Temperature")

plt.show()