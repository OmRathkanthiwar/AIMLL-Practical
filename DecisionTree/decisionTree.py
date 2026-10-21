import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# LOAD DATASET
df = pd.read_csv("Admission_Predict.csv")

# DATA PREPROCESSING
df.columns = df.columns.str.strip()
df = df.drop(columns=["Serial No."], errors="ignore")

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

# DECISION TREE MODEL
model = DecisionTreeClassifier(random_state=42)
model.fit(XTrain, yTrain)

# EVALUATION
yPred = model.predict(XTest)
print("Accuracy:", accuracy_score(yTest, yPred))
print("Confusion Matrix:\n", confusion_matrix(yTest, yPred))
print("Classification Report:\n", classification_report(yTest, yPred))

# TAKE USER INPUT
gre = float(input("Enter GRE Score: "))
toefl = float(input("Enter TOEFL Score: "))
rating = int(input("Enter University Rating (1-5): "))
sop = float(input("Enter SOP strength (1-5): "))
lor = float(input("Enter LOR strength (1-5): "))
cgpa = float(input("Enter CGPA (out of 10): "))
research = int(input("Research Experience (0=No, 1=Yes): "))

# PREDICT ADMISSION
student = pd.DataFrame([[
    gre, toefl, rating, sop, lor, cgpa, research
]], columns=X.columns)

prediction = model.predict(student)

if prediction[0] == 1:
    print("Student is likely to be admitted")
else:
    print("Student is unlikely to be admitted")