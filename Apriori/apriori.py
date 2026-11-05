import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

# LOAD DATASET
df = pd.read_csv("Market_Basket_Optimisation.csv", header=None)

# DATA PREPROCESSING
transactions = []

for i in range(len(df)):
    items = df.iloc[i].dropna().tolist()
    transactions.append(items)

print("Total Transactions:", len(transactions))

# APPLY APRIORI
rules = apriori(
    transactions,
    min_support=0.003,
    min_confidence=0.2,
    min_lift=3,
    min_length=2
)

rules = list(rules)

# DISPLAY RULES
for rule in rules:
    for item in rule.ordered_statistics:
        print(
            list(item.items_base), "=>", list(item.items_add),
            "Support:", round(rule.support, 3),
            "Confidence:", round(item.confidence, 3),
            "Lift:", round(item.lift, 3)
        )

# INCREASE MINIMUM CONFIDENCE
rules2 = apriori(
    transactions,
    min_support=0.003,
    min_confidence=0.4,
    min_lift=3,
    min_length=2
)

print("\nRules with Confidence 0.4:")

for rule in rules2:
    for item in rule.ordered_statistics:
        print(list(item.items_base), "=>", list(item.items_add))

# VISUALIZATION
support = []
confidence = []

for rule in rules:
    for item in rule.ordered_statistics:
        support.append(rule.support)
        confidence.append(item.confidence)

plt.scatter(support, confidence)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Association Rules")
plt.show()