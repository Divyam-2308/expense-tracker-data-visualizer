import streamlit as st
import pandas as pd
import sys
from pathlib import Path

#Add src to path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from src.expense_manager import ExpenseManager
from src.budget_manager import BudgetManager

# Page config
st.set_page_config(page_title="Budget",page_icon="💰",layout="wide")
st.title("💰 Budget Manager")
st.markdown("---")

# Initialize managers
em = ExpenseManager("data/expenses.csv")
bm = BudgetManager("data/budgets.json")

# Monthly Budget Section
st.subheader("🎯 Monthly Budget")

col1, col2 = st.columns(2)

with col1:
    current_budget = bm.get_monthly_budget()
    new_budget = st.number_input(
        "Set your monthly budget (₹)",
        min_value=0.0,
        value=float(current_budget),
        step=1000.0,
        format="%.0f"
    )
    if st.button("💾 Save Monthly Budget", use_container_width=True):
        bm.set_monthly_budget(new_budget)
        st.success(f" ✅ Monthly budget set to ₹{new_budget:.0f}")
        st.rerun()

with col2:
    total_spent = em.get_monthly_spending()
    remaining = bm.get_remaining_budget(total_spent)

    if current_budget > 0:
        progress = min(remaining['percentage_used'] / 100, 1.0)
        st.metric("Budget Used", f"{remaining['percentage_used']:.1f}%")
        st.progress(progress)

        if remaining['is_over_budget']:
            st.error(f"⚠️ You have exceeded your budget by ₹{abs(remaining['remaining']):.2f}!")
        else:
            st.success(f"✅ You have ₹{remaining['remaining']:.2f} left in your budget.")
    else:
        st.info("ℹ️ Please set a monthly budget to track your expenses.")

st.markdown("---")

#Category Budgets Section
st.subheader("📊 Category Budgets")

#Get current category budgets and spending
category_budgets = bm.get_all_category_budgets()
category_spending = em.get_category_totals()

CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Education", "Other"]

#Create a form for category budgets
with st.form("category_budgets_form"):
    st.markdown("Set budget limits for each category:")

    cols = st.columns(2)
    new_budget = {}

    for i, category in enumerate(CATEGORIES):
        with cols[i % 2]:
            current = category_budgets.get(category, 0.0)
            spent = category_spending.get(category, 0.0)

            new_budget[category] = st.number_input(
                f"{category} (Spent: ₹{spent:.2f})",
                min_value=0.0,
                value=float(current),
                step=500.0,
                format="%.0f",
                key=f"budget_{category}"
            )
    
    if st.form_submit_button("💾 Save Category Budgets", use_container_width=True):
        for category, amount in new_budget.items():
            if amount > 0:
                bm.set_category_budget(category, amount)
        st.success(" ✅ Category budgets updated successfully!")
        st.rerun()

st.markdown("---")

#Budget vs Spending Comparison
st.subheader("📈 Budget vs Actual Spending")

if category_budgets:
    comparison_data = []
    for category in CATEGORIES:
        budgeted = category_budgets.get(category, 0.0)
        spent = category_spending.get(category, 0.0)
        comparison_data.append({
            'Category': category,
            'Budget': budgeted,
            'Spent': spent,
            'Remaining': budgeted - spent,
            'Status': "Over Budget" if spent > budgeted else "Within Budget"
        })
    
    if comparison_data:
        df = pd.DataFrame(comparison_data)
        df['Budget'] = df['Budget'].apply(lambda x: f"₹{x:,.0f}")
        df['Spent'] = df['Spent'].apply(lambda x: f"₹{x:,.0f}")
        df['Remaining'] = df['Remaining'].apply(lambda x: f"₹{x:,.0f}")
        st.dataframe(df, use_container_width=True,hide_index=True)
    else:
        st.info("No budget data to compare")
else:
    st.info("Set category budgets above to see comparison")