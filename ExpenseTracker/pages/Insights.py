import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from src.expense_manager import ExpenseManager
from src.insights_generator import InsightsGenerator

# Page config
st.set_page_config(page_title="Expense Insights",page_icon="📈", layout="wide")
st.title("📈 Spending Insights")
st.markdown("---")

# Initialize
em = ExpenseManager("data/expenses.csv")

# Check if we have data
if len(em.df) == 0:
    st.warning("📭 No expenses recorded yet! Add some expenses to see insights.")
    st.stop()

insights = InsightsGenerator(em.df)
summary = insights.generate_summary()

# Key Insights Row
st.subheader("🔍 Key Insights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label ="📅 Daily Average Spending",
        value=f"₹{summary['daily_average']:.2f}",
    )

with col2:
    st.metric(
        label="📅 Weekly Average Spending",
        value=f"₹{summary['weekly_average']:.2f}",
    )

with col3:
    top_cat = summary['top_category']
    st.metric(
        label="🏆 Top Spending Category",
        value=top_cat['name'] if top_cat['name'] else "N/A",
        delta=f"₹{top_cat['amount']:.2f}" if top_cat['amount'] else None
        )

with col4:
    st.metric(
        label="📝 Total Transactions",
        value=f"{summary['transaction_count']}",
    )

st.markdown("---")

# Spending Trend
st.subheader("📊 Spending Trend")

trend = summary['trend']
if trend['trend'] == 'up':
    st.error(trend['message'])
elif trend['trend'] == 'down':
    st.success(trend['message'])
else:
    st.info(trend['message'])

col_left, col_right = st.columns(2)

with col_left:
    # Busiest Day
    busiest = summary.get('busiest_day', {})
    if busiest.get('day'):
        st.subheader("🗓️ Busiest Spending Day")
        st.info(f"You spend most on **{busiest['day']}s** (₹{busiest['amount']:,.0f} total)")

with col_right:
    # Largest Expense
    largest = summary.get('largest_expense')
    if largest:
        st.subheader("💸 Largest Single Expense")
        st.warning(f"**₹{largest['Amount']:,.0f}** on {largest['Category']}")
        if largest.get('Description'):
            st.caption(f"Description: {largest['Description']}")

st.markdown("---")

# Saving Tips
st.subheader("💡 Category Breakdown")

category_totals = summary.get('category_totals', {})
if category_totals:
    col1, col2 = st.columns(2)

    with col1:
        #Pie chart data
        chart_data = pd.DataFrame({
            'Category': list(category_totals.keys()),
            'Amount': list(category_totals.values())
        })
        chart_data = chart_data.set_index('Category')
        st.bar_chart(chart_data)
    
    with col2:
        # Table view
        table_data = pd.DataFrame({
            'Category': list(category_totals.keys()),
            'Amount': list(category_totals.values())
        })
        table_data = table_data.sort_values('Amount', ascending=False)
        table_data['Percentage'] = (table_data['Amount'] / table_data['Amount'].sum() * 100).round(1)
        table_data['Amount'] = table_data['Amount'].apply(lambda x: f"{x:,.0f}")
        table_data['Percentage'] = table_data['Percentage'].apply(lambda x: f"{x}%")
        st.dataframe(table_data, use_container_width=True,hide_index=True)

st.markdown("---")

# Monthly Comparison
st.subheader("📅 Monthly Spending Comparison")

#Group by month
em.df['Month'] = pd.to_datetime(em.df['Date']).dt.to_period('M')
monthly_spending = em.df.groupby('Month')['Amount'].sum()

if len(monthly_spending) > 0:
    monthly_df = monthly_spending.reset_index()
    monthly_df['Month'] = monthly_df['Month'].astype(str)
    monthly_df = monthly_df.set_index('Month')
    st.line_chart(monthly_df)
else:
    st.info("Not enough data to show monthly comparison.")