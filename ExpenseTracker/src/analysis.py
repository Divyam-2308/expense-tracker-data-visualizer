import pandas as pd 

#Load csv
df = pd.read_csv(r"ExpenseTracker\data\expenses.csv")

print(df.head())

print("\nBasic Info")
print(df.describe())

total = df["Amount"].sum()
print(f"\n Total Spending: ${total}")