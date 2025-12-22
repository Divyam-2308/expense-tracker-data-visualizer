import json
from pathlib import Path
from datetime import datetime
from typing import Optional

class BudgetManager:
    """Manages budget settings and tracking"""

    DEFAULT_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Other"]

    def __init__(self, budget_path: str = "data/budgets.json"):
        self.budget_path = Path(budget_path)
        self.budgets = self._load_budgets()
    
    def _load_budgets(self) -> dict:
        """Load budgets from JSON file"""
        if self.budget_path.exists():
            with open(self.budget_path, 'r') as f:
                return json.load(f)
        
        return {
            "monthly_budget" : 0,
            "categories": {},
            "created_at": datetime.now().isoformat()
        }
    
    def _save_budgets(self):
        """Save budgets to JSON file"""
        self.budget_path.parent.mkdir(parents=True, exist_ok=True)
        self.budgets["updated_at"] = datetime.now().isoformat()
        with open(self.budget_path, 'w') as f:
            json.dump(self.budgets, f, indent=2)
    
    def set_monthly_budget(self, amount: float):
        """Set the overall monthly budget"""
        if amount < 0:
            raise ValueError("Budget amount cannot be negative")
        self.budgets["monthly_budget"] = amount
        self._save_budgets()
    
    def get_monthly_budget(self) -> float:
        """Get total monthly budget"""
        return self.budgets.get("monthly_budget", 0)
    
    def set_category_budget(self, category: str, amount: float):
        """Set budget for a specific category"""
        if amount < 0:
            raise ValueError("Budget amount cannot be negative")
        self.budgets["categories"][category] = amount
        self._save_budgets()
    
    def get_category_budget(self, category: str) -> float:  
        """Get budget for a specific category"""
        return self.budgets["categories"].get(category, 0)
    
    def get_all_category_budgets(self) -> dict:
        """Get all category budgets"""
        return self.budgets.get("categories", {})
    
    def remove_category_budget(self, category: str) -> bool:
        """Remove budget for a category"""
        if category in self.budgets["categories"]:
            del self.budgets["categories"][category]
            self._save_budgets()
            return True
        return False
    
    def check_budget_status(self, spend_by_category: dict) -> list:
        """
        Check spending against budgets
        
        Args:
            spent_by_category: Dict of {category: amount_spent}
        
        Returns:
            List of warning dictionaries
        """
        warnings = []

        # Check each category budget
        for category, limit in self.budgets["categories"].items():
            if limit <= 0:
                continue
            current = spend_by_category.get(category, 0)
            percentage = (current / limit) * 100 

            warning ={
                "category": category,
                "spent": current,
                "limit": limit,
                "percentage": percentage
            }
            if percentage >= 100:
                warning["type"] = "exceeded"
                warning["severity"] = "high"
                warning["message"] = f"🚨 {category}: Exceeded by ₹{current - limit:,.0f}"
            elif percentage >= 80:
                warning["type"] = "warning"
                warning["severity"] = "medium"
                warning["message"] = f"⚠️ {category}: {percentage:.0f}% of budget used"
            elif percentage >= 50:
                warning["type"] = "info"
                warning["severity"] = "low"
                warning["message"] = f"ℹ️ {category}: {percentage:.0f}% of budget used"
            else:
                continue
            warnings.append(warning)
        
        #Sort by severity
        severity_order = {"high": 0, "medium": 1, "low": 2}
        warnings.sort(key=lambda x: severity_order[x["severity"]]) 

        return warnings

    def get_remaining_budget(self, total_spent: float) -> dict:
        """Get remaining budget info"""
        monthly = self.get_monthly_budget()
        remaining = monthly - total_spent
        percentage_used = (total_spent / monthly) * 100 if monthly > 0 else 0

        return {
            "monthly_budget": monthly,
            "total_spent": total_spent,
            "remaining": remaining,
            "percentage_used": percentage_used,
            "is_over_budget": remaining < 0
        }
    
       