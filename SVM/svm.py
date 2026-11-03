import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# LOAD DATASET
df = pd.read_csv("train.csv")

# INPUT AND OUTPUT
X = df.drop(columns=["price_range"])
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

battery_power = float(input("Enter Battery Power: "))
blue = float(input("Bluetooth (0/1): "))
clock_speed = float(input("Enter Clock Speed: "))
dual_sim = float(input("Dual SIM (0/1): "))
fc = float(input("Enter Front Camera: "))
four_g = float(input("4G (0/1): "))
int_memory = float(input("Enter Internal Memory: "))
m_dep = float(input("Enter Mobile Depth: "))
mobile_wt = float(input("Enter Mobile Weight: "))
n_cores = float(input("Enter Number of Cores: "))
pc = float(input("Enter Primary Camera: "))
px_height = float(input("Enter Pixel Height: "))
px_width = float(input("Enter Pixel Width: "))
ram = float(input("Enter RAM: "))
sc_h = float(input("Enter Screen Height: "))
sc_w = float(input("Enter Screen Width: "))
talk_time = float(input("Enter Talk Time: "))
three_g = float(input("3G (0/1): "))
touch_screen = float(input("Touch Screen (0/1): "))
wifi = float(input("WiFi (0/1): "))

# CREATE INPUT DATAFRAME

features = [[
    battery_power, blue, clock_speed, dual_sim, fc, four_g,
    int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
    px_width, ram, sc_h, sc_w, talk_time, three_g,
    touch_screen, wifi
]]

phone = pd.DataFrame(features, columns=X.columns)

# PREDICTION

phone = scaler.transform(phone)
prediction = model.predict(phone)

print("Predicted Price Range:", prediction[0])