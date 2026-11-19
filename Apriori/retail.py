import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# LOAD DATASET
df = pd.read_csv("transactions.csv")

# DATA PREPROCESSING
transactions = df.groupby("CustomerID")["ProductID"].apply(list).tolist()

# CONVERT TRANSACTIONS INTO BOOLEAN DATA
te = TransactionEncoder()
teArray = te.fit(transactions).transform(transactions)

dfEncoded = pd.DataFrame(teArray, columns=te.columns_)

# APPLY APRIORI ALGORITHM
frequentItems = apriori(
    dfEncoded,
    min_support=0.01,
    use_colnames=True
)

print("Frequent Itemsets:")
print(frequentItems)

# GENERATE ASSOCIATION RULES
rules = association_rules(
    frequentItems,
    metric="confidence",
    min_threshold=0.2
)

print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support",
             "confidence", "lift"]])

# EVALUATION
print("\nNumber of Frequent Itemsets:", len(frequentItems))
print("Number of Association Rules:", len(rules))

print("\nAverage Support:", rules["support"].mean())
print("Average Confidence:", rules["confidence"].mean())
print("Average Lift:", rules["lift"].mean())

# VISUALIZATION
plt.scatter(rules["support"], rules["confidence"],
            c=rules["lift"], cmap="viridis")
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Apriori Association Rules")
plt.colorbar(label="Lift")
plt.show()
