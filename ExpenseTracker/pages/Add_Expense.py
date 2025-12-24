import streamlit as st
import sys
from pathlib import Path
from datetime import date, datetime
import pandas as pd

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from src.expense_manager import ExpenseManager

#Page config
st.set_page_config(page_title="Add Expense",page_icon="➕",layout="wide")
st.title("➕ Add Expense")
st.markdown("----")

# Initialize manager
em = ExpenseManager("data/expenses.csv")

#Categories
em = ExpenseManager("data/expenses.csv")

# Categories
CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Bills",
    "Education",
    "Other"
]
# Expense Form
st.subheader("Add a New Expense")

with st.form("expense_form",clear_on_submit=True):
    col1,col2 = st.columns(2)

    with col1:
        expense_date = st.date_input(
            "📅 Date",
            value=date.today(),
            max_value=date.today()
        )

        category = st.selectbox(
            "🏷️ Category",
            options=CATEGORIES
        )
    
    with col2:
        amount = st.number_input(
            "💰 Amount (₹)",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

        description = st.text_input(
            "📝 Description (Optional)",
            placeholder="e.g., Lunch at Cafe"
        )
    submitted = st.form_submit_button("Add Expense", use_container_width=True)

    if submitted:
        if amount <= 0:
            st.error("❗ Amount must be greater than zero.")
        else:
            try:
                em.add_expense(
                    date=expense_date.strftime("%Y-%m-%d"),
                    category=category,
                    amount=amount,
                    description=description
                )
                st.success(f"✔️ Added ₹{amount:.2f} to {category} on {expense_date.strftime('%Y-%m-%d')}.")
                st.balloons()
            except Exception as e:
                st.error(f"❗ Failed to add expense: {e}")

st.markdown("----")

#Quick add buttons
st.subheader(" ⚡ Quick Add")
st.markdown("Add common expenses with one click:")

quick_col1, quick_col2, quick_col3, quick_col4= st.columns(4)

with quick_col1:
    if st.button(" ☕️ Coffee-50",use_container_width=True):
        em.add_expense(date.today().strftime("%Y-%m-%d"), "Food", 50, "Coffee")
        st.success("☕ Added!")
        st.rerun()

with quick_col2:
    if st.button(" 🚕 Cab-100",use_container_width=True):
        em.add_expense(date.today().strftime("%Y-%m-%d"), "Transport", 100, "Cab Ride")
        st.success("🚕 Added!")
        st.rerun()

with quick_col3:
    if st.button(" 🍔 Meal-200",use_container_width=True):
        em.add_expense(date.today().strftime("%Y-%m-%d"), "Food", 200, "Meal")
        st.success("🍔 Added!")
        st.rerun()

with quick_col4:
    if st.button(" 🎬 Movie-300",use_container_width=True):
        em.add_expense(date.today().strftime("%Y-%m-%d"), "Entertainment", 300, "Movie Ticket")
        st.success("🎬 Added!")
        st.rerun()

st.markdown("----")

#Recent Expenses Preview
st.subheader("📋 Recent Expenses")
recent = em.get_recent_expenses(5)
if len(recent) > 0:
    display_df = recent.copy()
    display_df['Date'] = pd.to_datetime(display_df['Date']).dt.strftime('%Y-%m-%d')
    display_df['Amount'] = display_df['Amount'].apply(lambda x: f"₹{x:,.0f}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)
else:
    st.info("No expenses recorded yet.")