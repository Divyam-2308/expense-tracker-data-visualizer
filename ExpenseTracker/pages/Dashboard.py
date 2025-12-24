import streamlit as st
import pandas as pd
import sys 
from pathlib import Path

#Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from src.expense_manager import ExpenseManager
from src.budget_manager import BudgetManager

#Page config
st.set_page_config(page_title="Dashboard",page_icon="📊",layout="wide")
st.title("📊 Dashboard")
st.markdown("----")

# Initialize managers
em = ExpenseManager("data/expenses.csv")
bm = BudgetManager("data/budgets.json")

# Check if we have data
if len(em.df) == 0:
    st.warning("📭 No expenses recorded yet! Go to **Add Expense** to get started.")
    st.stop()

#Key Metrics Row
st.subheader("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

total_spent = em.get_total_spent()
monthly_budget = bm.get_monthly_budget()
remaining = monthly_budget - total_spent if monthly_budget > 0 else 0
transaction_count = len(em.df)

with col1:
    st.metric(
        label="💸 Total Spent",
        value=f"{total_spent:,.0f}"
    )

with col2:
    st.metric(
        label="🎯 Monthly Budget",
        value=f"₹{monthly_budget:,.0f}" if monthly_budget > 0 else "Not Set"
    )

with col3:
    if monthly_budget > 0:
        delta_color = "normal" if remaining >= 0 else "inverse"
        st.metric(
            label= "🛡️ Remaining Budget",
            value=f"₹{remaining:,.0f}",
            delta=f"{(remaining / monthly_budget)*100:.0f}%" if monthly_budget > 0 else "N/A",
            delta_color=delta_color
        )
    else:
        st.metric(label="🛡️ Remaining Budget", value="Set Budget")

with col4:
    st.metric(
        label="🧾 Transactions",
        value=f"{transaction_count}"
    )

st.markdown("----")

#Budget Warnings
warnings = bm.check_budget_status(em.get_category_totals())
if warnings:
    st.subheader("⚠️ Budget Warnings")
    for w in warnings:
        if w["severity"] == "high":
            st.error(w["message"])
        elif w["severity"] == "medium":
            st.warning(w["message"])
        else:
            st.info(w["message"])
    st.markdown("----")

#Charts Row
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Spending by Category")
    category_totals = em.get_category_totals() 
    category_totals = em.get_category_totals()
    if category_totals:
        chart_data = pd.DataFrame({
            'Category': list(category_totals.keys()),
            'Amount': list(category_totals.values())
        })
        chart_data = chart_data.set_index('Category')
        st.bar_chart(chart_data)
    else:
        st.info("No expense data to display.")

st.markdown("----")

#Recent Transactions
st.subheader("📋 Recent Transactions")
recent = em.get_recent_expenses(10)
if len(recent) > 0:
    # Format for display
    display_df = recent.copy()
    display_df['Date'] = pd.to_datetime(display_df['Date']).dt.strftime('%Y-%m-%d')
    display_df['Amount'] = display_df['Amount'].apply(lambda x: f"₹{x:,.0f}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)
else:
    st.info("No transactions yet")