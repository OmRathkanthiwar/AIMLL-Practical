import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

# LOAD DATASET
df = pd.read_csv("Market_Basket_Optimisation.csv", header=None)

print(df.head())

# DATA PREPROCESSING
transactions = []

for i in range(len(df)):
    items = []
    for j in range(len(df.columns)):
        if pd.notna(df.iloc[i, j]):
            items.append(str(df.iloc[i, j]).strip())
    transactions.append(items)

print("Total Transactions:", len(transactions))

# APPLY APRIORI ALGORITHM
rules = apriori(
    transactions,
    min_support=0.003,
    min_confidence=0.2,
    min_lift=3,
    min_length=2
)

rules = list(rules)

# DISPLAY RULES
ruleData = []

for rule in rules:
    for item in rule.ordered_statistics:
        ruleData.append([
            list(item.items_base),
            list(item.items_add),
            rule.support,
            item.confidence,
            item.lift
        ])

result = pd.DataFrame(
    ruleData,
    columns=["Antecedent", "Consequent", "Support", "Confidence", "Lift"]
)

print("Total Rules:", len(result))
print(result)

# INCREASE MINIMUM CONFIDENCE
rules2 = apriori(
    transactions,
    min_support=0.003,
    min_confidence=0.4,
    min_lift=3,
    min_length=2
)

print("\nRules with Minimum Confidence 0.4:")

for rule in rules2:
    for item in rule.ordered_statistics:
        print(
            list(item.items_base), "=>", list(item.items_add),
            "Support:", round(rule.support, 3),
            "Confidence:", round(item.confidence, 3),
            "Lift:", round(item.lift, 3)
        )

# VISUALIZE RULES
if not result.empty:
    plt.scatter(result["Support"], result["Confidence"])
    plt.xlabel("Support")
    plt.ylabel("Confidence")
    plt.title("Association Rules using Apriori")
    plt.show()
else:
    print("No rules found.")
