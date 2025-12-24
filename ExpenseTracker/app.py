import streamlit as st

#Page configuration
st.set_page_config(
    page_title="Smart Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Main title
st.title("💰 Smart Expense Tracker")
st.markdown("----")

# Welcome message
st.markdown("""
### Welcome to Your Personal Finance Manager! 👋

This app helps you:
- 📊 **Track** your daily expenses
- 💰 **Set budgets** and get alerts
- 📈 **Analyze** your spending patterns
- 💡 **Get tips** to save money

---

### 🧭 How to Navigate

Use the **sidebar** on the left to access different features:

| Page | What it does |
|------|--------------|
| 📊 **Dashboard** | See your spending overview and charts |
| ➕ **Add Expense** | Record a new expense |
| 💰 **Budget** | Set and manage your budgets |
| 📈 **Insights** | Get analytics and saving tips |

---

### 🚀 Get Started

👈 Click on **Dashboard** in the sidebar to see your spending overview!
""")
# Footer
st.markdown("----")
st.markdown("Developed with ❤️ using Streamlit")