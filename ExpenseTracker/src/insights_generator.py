import pandas as pd
from datetime import datetime, timedelta

class InsightsGenerator:
    """Generates insights and analytics from expense data."""

    def __init__(self, expense_df: pd.DataFrame):
        self.df = expense_df.copy()
        if len(self.df) > 0:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
    
    def get_top_spending_category(self) -> tuple:
        """
        Get the category with highest spending 

        Returns:
            (category_name, amount) or (None, 0) if no data
        """
        if len(self.df) == 0:
            return (None, 0)
        
        totals = self.df.groupby('Category')['Amount'].sum()
        top_category = totals.idxmax()
        return (top_category, totals[top_category])
    
    def get_lowest_spending_category(self) -> tuple:
        """
        Get the category with lowest spending 

        Returns:
            (category_name, amount) or (None, 0) if no data
        """
        if len(self.df) == 0:
            return (None, 0)
        
        totals = self.df.groupby('Category')['Amount'].sum()
        low_category = totals.idxmin()
        return (low_category, totals[low_category])
    
    def get_daily_average(self) -> float:
        """Calculate average daily spending"""
        if len(self.df) == 0:
            return 0
        date_range = (self.df['Date'].max() - self.df['Date'].min()).days
        return self.df['Amount'].sum() / max(date_range, 1)

    def get_weekly_average(self) -> float:
        """Calculate average weekly spending"""
        return self.get_daily_average() * 7
    
    def get_spending_trend(self) ->dict:
        """Compare this week vs last week spending"""
        if len(self.df) == 0:
            return {"trend": "neutral", "message": "No data available", "change": 0}
        
        today = datetime.now()
        this_week_start = today - timedelta(days=7)
        last_week_start = today - timedelta(days=14)

        this_week = self.df[self.df['Date'] >= this_week_start]['Amount'].sum()
        last_week = self.df[
            (self.df['Date'] >= last_week_start) & 
            (self.df['Date'] < this_week_start)
        ]['Amount'].sum()
        if last_week == 0:
            return {"trend": "neutral", "message": "No data for last week", "change": 0}
        
        change = ((this_week - last_week) / last_week) * 100

        if change > 10:
            return {
                "trend":"up",
                "message": f"Spending UP {(change):.0f}% vs last week",
                "change": change,
                "this_week": this_week,
                "last_week": last_week
            }
        elif change < -10:
            return {
                "trend":"down",
                "message": f"Spending DOWN {abs(change):.0f}% vs last week",
                "change": change,
                "this_week": this_week,
                "last_week": last_week
            }
        else:
            return {
                "trend":"neutral",
                "message": "Spending stable vs last week",
                "change": change,
                "this_week": this_week,
                "last_week": last_week
            }
    
    def get_busiest_spending_day(self) -> tuple:
        """Find which day of week has highest spending"""
        if len(self.df) == 0:
            return (None, 0)
        
        self.df['DayOfWeek'] = pd.to_datetime(self.df['Date']).dt.day_name()
        day_totals = self.df.groupby('DayOfWeek')['Amount'].sum()
        busiest_day = day_totals.idxmax()
        return (busiest_day, day_totals[busiest_day])
    
    def get_largest_expense(self) -> dict | None:
        """Get the single largest expense"""
        if len(self.df) == 0:
            return None
        
        idx = self.df['Amount'].idxmax()
        row = self.df.loc[idx]
        return {
            "Date": row['Date'],
            "Category": row['Category'],
            "Amount": row['Amount'],
            "Description": row.get('Description','')
        }
    
    def get_savings_tips(self,category_totals: dict) -> list:
        """Generate personalized saving tips"""
        tips = []

        if not category_totals:
            return ["Start tracking expenses to get personalized tips!"]
        
        top_cat, top_amount = self.get_top_spending_category()

        if top_cat:
            potential_saving = top_amount * 0.2
            tips.append(f" Reducing {top_cat} by 20% could save {potential_saving:,.0f}")
        
        daily_avg = self.get_daily_average()
        if daily_avg > 0:
            tips.append(f"💡 Your daily average is {daily_avg:,.0f}. Try a no-spend day once a week!")
        
        trend = self.get_spending_trend()
        if trend['trend'] == 'up':
            tips.append("💡 Your spending is increasing. Review recent purchases.")
        
        if "Food" in category_totals and category_totals["Food"] > 3000:
            tips.append(" 💡Consider meal prepping to reduce food expenses.")
        
        if "Entertainment" in category_totals and category_totals["Entertainment"] > 2000:
            tips.append(" 💡Look for free or low-cost entertainment options.")
        
        return tips if tips else [" ✨ Great job! Your spending seems well managed."]
    
    def generate_summary(self) -> dict:
        """Generate complete insights summary"""
        top_cat, top_amount = self.get_top_spending_category()
        low_cat, low_amount = self.get_lowest_spending_category()
        largest = self.get_largest_expense()
        busiest_day, day_amount = self.get_busiest_spending_day()

        return {
            "total_spent": self.df['Amount'].sum() if len(self.df) > 0 else 0,
            "transaction_count": len(self.df),
            "daily_average": self.get_daily_average(),
            "weekly_average": self.get_weekly_average(),
            "top_category": {"name": top_cat,"amount": top_amount},
            "lowest_category": {"name": low_cat,"amount": low_amount},
            "largest_expense": largest,
            "busiest_day": {"name": busiest_day,"amount": day_amount},
            "trend": self.get_spending_trend(),
        }