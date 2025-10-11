import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from filter_utils import filter_by_date

# Read data
df = pd.read_csv(r"ExpenseTracker\data\expenses.csv")

import matplotlib.pyplot as plt

filtered = filter_by_date(df, "2025-01-01", "2025-05-05")

daily_total = filtered.groupby("Date")["Amount"].sum()
daily_total.plot(kind="line", marker="o", color="orange")

plt.title("Expenses Between Selected Dates")
plt.xlabel("Date")
plt.ylabel("Amount (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()


