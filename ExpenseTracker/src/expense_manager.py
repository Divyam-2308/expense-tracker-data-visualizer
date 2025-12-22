import pandas as pd
from pathlib import Path #Pathlib(A GPS to handle file system paths)
from datetime import datetime
from typing import Optional #For type hinting

class ExpenseManager:
    """Manages all expense-related operations"""
    
    def __init__(self, data_path: str = "data/expenses.csv"):
        self.data_path = Path(data_path)
        self.df = self._load_data()
    
    def _load_data(self) -> pd.DataFrame: #(_) means it's a private method
        """Load expenses from CSV file"""
        if self.data_path.exists():
            df = pd.read_csv(self.data_path)
            df['Date'] = pd.to_datetime(df['Date'])
            return df
        # Return empty DataFrame with proper dtypes to avoid FutureWarning
        return pd.DataFrame({
            'Date': pd.Series(dtype='datetime64[ns]'),
            'Category': pd.Series(dtype='str'),
            'Amount': pd.Series(dtype='float64'),
            'Description': pd.Series(dtype='str')
        })
    
    def _save_data(self):
        """Save expenses to CSV file"""
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.data_path, index=False)
    
    def add_expense(self, date: str, category: str, amount: float, description: str = "") -> bool: 
        """
        Add a new expense entry
        
        Args:
            date: Date string (YYYY-MM-DD)
            category: Expense category
            amount: Amount spent
            description: Optional description
        
        Returns:
            True if successful
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        new_row = {
            'Date': pd.to_datetime(date),
            'Category': category,
            'Amount': amount,
            'Description': description
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self._save_data()
        return True
    
    def delete_expense(self, index: int) -> bool:
        """Delete expense by index"""
        if 0 <= index < len(self.df):
            self.df = self.df.drop(index).reset_index(drop=True)
            self._save_data()
            return True
        return False
    
    def get_total_spent(self) -> float:
        """Get total amount spent"""
        return self.df['Amount'].sum()
    
    def get_category_totals(self) -> dict:
        """Get total spending per category"""
        if len(self.df) == 0: 
            return {} # Return empty dict if no data
        return self.df.groupby('Category')['Amount'].sum().to_dict()
    
    def get_monthly_spending(self, year: Optional[int] = None, month: Optional[int] = None) -> float:
        """
        Get spending for a specific month
        Defaults to current month if not specified
        """
        if year is None:
            year = datetime.now().year
        if month is None:
            month = datetime.now().month
            
        mask = (self.df['Date'].dt.year == year) & (self.df['Date'].dt.month == month)
        return self.df[mask]['Amount'].sum()
    
    def get_expenses_by_date_range(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Get expenses between two dates"""
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)
        mask = (self.df['Date'] >= start) & (self.df['Date'] <= end)
        return self.df[mask]
    
    def get_expenses_by_category(self, category: str) -> pd.DataFrame:
        """Get all expenses for a category"""
        return self.df[self.df['Category'] == category]
    
    def get_all_categories(self) -> list:
        """Get list of all unique categories"""
        return self.df['Category'].unique().tolist()
    
    def get_recent_expenses(self, count: int = 10) -> pd.DataFrame:
        """Get most recent expenses"""
        return self.df.sort_values('Date', ascending=False).head(count)