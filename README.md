# 💰 Smart Expense Tracker

A personal finance management app built with Python and Streamlit.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red)

## 🌟 Features

- 📊 **Dashboard** - View spending overview and charts
- ➕ **Add Expenses** - Quick and easy expense entry
- 💰 **Budget Management** - Set monthly and category budgets
- 📈 **Insights** - Get spending analytics and saving tips
- ⚠️ **Alerts** - Budget warnings when overspending

## 🚀 Live Demo

👉 [Open App](https://your-app-name.streamlit.app)

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Add Expense
![Add Expense](screenshots/add-expense.png)

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **Data Storage**: CSV, JSON

## 📁 Project Structure

```
ExpenseTracker/
├── app.py                  # Main application
├── pages/
│   ├── 1_📊_Dashboard.py   # Dashboard page
│   ├── 2_➕_Add_Expense.py # Add expense page
│   ├── 3_💰_Budget.py      # Budget management
│   └── 4_📈_Insights.py    # Analytics page
├── src/
│   ├── expense_manager.py  # Expense operations
│   ├── budget_manager.py   # Budget operations
│   └── insights_generator.py # Analytics
└── data/
    ├── expenses.csv        # Expense data
    └── budgets.json        # Budget settings
```

## 🏃 Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/expense-tracker.git

# Navigate to project
cd expense-tracker/ExpenseTracker

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).