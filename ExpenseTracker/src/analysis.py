import pandas as pd 
from filter_utils import filter_by_date



#Load csv
df = pd.read_csv(r"ExpenseTracker\data\expenses.csv")

# print(df.head())

filtered_df = filter_by_date(df, "2025-01-01", "2025-10-05")
print(filtered_df)


# print("\nBasic Info")
# print(df.describe())

# total = df["Amount"].sum()
# print(f"\n Total Spending: ${total}")