<div align="center">

# 💰 CashCraft

### Your Personal Finance Command Center

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Deployed](https://img.shields.io/badge/Deployed-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit)](https://cashcraft.streamlit.app)

[Live Demo](https://cashcraft.streamlit.app) • [Report Bug](https://github.com/Divyam-2308/expense-tracker-data-visualizer/issues) • [Request Feature](https://github.com/Divyam-2308/expense-tracker-data-visualizer/issues)

---

<img src="screenshots/dashboard-preview.png" alt="CashCraft Dashboard" width="800">

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About

**CashCraft** is a smart expense tracking application that helps you take control of your finances. Built with Python and Streamlit, it provides an intuitive interface to track spending, set budgets, and gain insights into your financial habits.

### Why CashCraft?

| Problem | CashCraft Solution |
|---------|-------------------|
| 😵 Losing track of expenses | 📊 Visual dashboard with real-time tracking |
| 💸 Overspending on categories | ⚠️ Smart budget alerts before you exceed |
| 🤔 No idea where money goes | 📈 Detailed insights and category breakdown |
| 📝 Complex finance apps | ✨ Simple, clean, and easy-to-use interface |

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📊 Dashboard
- Real-time spending overview
- Interactive charts
- Budget progress tracking
- Recent transactions

</td>
<td width="50%">

### ➕ Quick Expense Entry
- Simple form input
- One-click quick add buttons
- Category selection
- Date picker

</td>
</tr>
<tr>
<td width="50%">

### 💰 Budget Management
- Monthly budget limits
- Category-wise budgets
- Visual progress bars
- Budget vs Actual comparison

</td>
<td width="50%">

### 📈 Smart Insights
- Spending trends analysis
- Daily/Weekly averages
- Top spending categories
- Personalized saving tips

</td>
</tr>
</table>

### 🔔 Alert System

```
🟢 Under 50%  → You're on track!
🟡 50-80%     → Careful, spending increasing
🟠 80-100%    → Warning! Almost at limit
🔴 Over 100%  → Budget exceeded!
```

---

## 📸 Screenshots

<details>
<summary><b>📊 Dashboard</b> (Click to expand)</summary>
<br>
<img src="screenshots/dashboard.png" alt="Dashboard" width="700">
<p><i>Overview of your spending with key metrics and charts</i></p>
</details>

<details>
<summary><b>➕ Add Expense</b> (Click to expand)</summary>
<br>
<img src="screenshots/add-expense.png" alt="Add Expense" width="700">
<p><i>Quick and easy expense entry with form and quick-add buttons</i></p>
</details>

<details>
<summary><b>💰 Budget Manager</b> (Click to expand)</summary>
<br>
<img src="screenshots/budget.png" alt="Budget Manager" width="700">
<p><i>Set and track budgets for overall and category-wise spending</i></p>
</details>

<details>
<summary><b>📈 Insights</b> (Click to expand)</summary>
<br>
<img src="screenshots/insights.png" alt="Insights" width="700">
<p><i>Detailed analytics and personalized saving tips</i></p>
</details>

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=python" width="48" height="48" alt="Python" />
<br>Python
</td>
<td align="center" width="96">
<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="48" height="48" alt="Streamlit" />
<br>Streamlit
</td>
<td align="center" width="96">
<img src="https://pandas.pydata.org/static/img/pandas_mark.svg" width="48" height="48" alt="Pandas" />
<br>Pandas
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=git" width="48" height="48" alt="Git" />
<br>Git
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=github" width="48" height="48" alt="GitHub" />
<br>GitHub
</td>
</tr>
</table>

| Category | Technology |
|----------|------------|
| **Language** | Python 3.12 |
| **Framework** | Streamlit |
| **Data Processing** | Pandas |
| **Data Storage** | CSV, JSON |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Divyam-2308/expense-tracker-data-visualizer.git
   cd expense-tracker-data-visualizer
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   cd ExpenseTracker
   streamlit run app.py
   ```

5. **Open your browser**
   ```
   http://localhost:8501
   ```

---

## 📁 Project Structure

```
expense-tracker/
│
├── 📂 ExpenseTracker/
│   ├── 📄 app.py                    # Main application entry
│   │
│   ├── 📂 pages/                    # Streamlit pages
│   │   ├── 📄 1_📊_Dashboard.py     # Dashboard page
│   │   ├── 📄 2_➕_Add_Expense.py   # Add expense page
│   │   ├── 📄 3_💰_Budget.py        # Budget management
│   │   └── 📄 4_📈_Insights.py      # Analytics & insights
│   │
│   ├── 📂 src/                      # Core logic
│   │   ├── 📄 expense_manager.py    # Expense CRUD operations
│   │   ├── 📄 budget_manager.py     # Budget management
│   │   └── 📄 insights_generator.py # Analytics engine
│   │
│   └── 📂 data/                     # Data storage
│       ├── 📄 expenses.csv          # Expense records
│       └── 📄 budgets.json          # Budget settings
│
├── 📂 screenshots/                  # App screenshots
├── 📄 requirements.txt              # Dependencies
├── 📄 .gitignore                    # Git ignore rules
├── 📄 LICENSE                       # MIT License
└── 📄 README.md                     # You are here!
```

---

## 💡 Usage

### Adding an Expense

```python
# The app handles this through UI, but internally:
expense_manager.add_expense(
    date="2024-12-25",
    category="Food",
    amount=250.00,
    description="Christmas dinner"
)
```

### Setting a Budget

```python
# Set monthly budget
budget_manager.set_monthly_budget(15000)

# Set category budget
budget_manager.set_category_budget("Food", 5000)
```

### Getting Insights

```python
# Generate spending summary
insights = InsightsGenerator(expense_df)
summary = insights.generate_summary()

# Get saving tips
tips = insights.get_savings_tips(category_totals)
```

---

## 🗺️ Roadmap

- [x] Basic expense tracking
- [x] Budget management
- [x] Spending insights
- [x] Streamlit deployment
- [ ] 📱 Mobile-responsive design improvements
- [ ] 📊 Export reports (PDF/Excel)
- [ ] 🔐 User authentication
- [ ] 💳 Bank statement import
- [ ] 🤖 AI-powered spending predictions
- [ ] 📧 Email alerts for budget warnings

See the [open issues](https://github.com/Divyam-2308/expense-tracker-data-visualizer/issues) for a full list of proposed features.

---

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

```
MIT License

Copyright (c) 2025 Divyam Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Contact

**Divyam Jain**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/divyam2308)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Divyam-2308)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jaindivyam200@gmail.com)

**Project Link:** [https://github.com/Divyam-2308/expense-tracker-data-visualizer](https://github.com/Divyam-2308/expense-tracker-data-visualizer)

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

Made with ❤️ and ☕ by [Divyam Jain](https://github.com/Divyam-2308)

</div>