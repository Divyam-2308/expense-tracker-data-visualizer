import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 1)
num_days = 30 

dates = [start_date + timedelta(days=random.randint(0, num_days - 1)) for _ in range(20)]

categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Health", "Savings", "Miscellaneous"]
descriptions = {
    "Food": ["Lunch", "Dinner", "Snacks", "Breakfast"],
    "Travel": ["Auto fare", "Bus ticket", "Fuel", "Metro card"],
    "Shopping": ["T-shirt", "Shoes", "Watch", "Bag"],
    "Bills": ["Electricity", "Internet", "Phone recharge"],
    "Entertainment": ["Movie", "Subscription", "Game"],
    "Health": ["Medicines", "Doctor visit"],
    "Savings": ["Added to savings"],
    "Miscellaneous": ["Stationery", "Gift"]
}

data = []
for i in range(20):
    category = random.choice(categories)
    desc = random.choice(descriptions[category])
    amount = round(random.uniform(50, 2000), 2)
    data.append([dates[i].strftime("%Y-%m-%d"), category, desc, amount])

df = pd.DataFrame(data, columns=["Date", "Category", "Description", "Amount"])

# --- Step 5: Sort by Date ---
df = df.sort_values("Date")

# --- Step 6: Save as CSV ---
df.to_csv("D:\\expense-tracker-data-visualizer\\ExpenseTracker\\data\\expenses.csv", index=False)

print("✅ expenses.csv file created successfully!")
print(df.head())