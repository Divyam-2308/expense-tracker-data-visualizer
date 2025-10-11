import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"ExpenseTracker\data\expenses.csv")

category_total = df.groupby("Category")["Amount"].sum()


plt.figure(figsize=(7,5))
category_total.plot(kind="bar",color="skyblue",edgecolor="black")
plt.title("Total Spending by Category",fontsize=14)
plt.xlabel("Category")
plt.ylabel("Total Amount ($)")
plt.tight_layout()
plt.show()
