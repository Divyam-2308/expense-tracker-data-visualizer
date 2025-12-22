from src.expense_manager import ExpenseManager
from src.budget_manager import BudgetManager
from src.insights_generator import InsightsGenerator

def run_integration_test():
    print("🧪 INTEGRATION TEST")
    print("=" * 50)
    
    # 1. Initialize all managers
    print("\n1️⃣ Initializing managers...")
    em = ExpenseManager("data/test_expenses.csv")
    bm = BudgetManager("data/test_budgets.json")
    
    # 2. Set up budgets
    print("2️⃣ Setting up budgets...")
    bm.set_monthly_budget(15000)
    bm.set_category_budget("Food", 4000)
    bm.set_category_budget("Transport", 2000)
    bm.set_category_budget("Entertainment", 2000)
    
    # 3. Add expenses
    print("3️⃣ Adding expenses...")
    em.add_expense("2024-12-21", "Food", 350, "Restaurant dinner")
    em.add_expense("2024-12-21", "Transport", 150, "Cab to office")
    em.add_expense("2024-12-20", "Food", 3800, "Weekly groceries")
    em.add_expense("2024-12-19", "Entertainment", 1200, "Movie night")
    em.add_expense("2024-12-18", "Transport", 1900, "Monthly metro pass")
    
    # 4. Check budget status
    print("4️⃣ Checking budget status...")
    spent = em.get_category_totals()
    warnings = bm.check_budget_status(spent)
    
    print(f"\n   Spending by category: {spent}")
    if warnings:
        print("   ⚠️ Budget Warnings:")
        for w in warnings:
            print(f"      {w['message']}")
    else:
        print("   ✅ All budgets on track!")
    
    # 5. Generate insights
    print("\n5️⃣ Generating insights...")
    insights = InsightsGenerator(em.df)
    summary = insights.generate_summary()
    
    print(f"   💰 Total Spent: ₹{summary['total_spent']:,.0f}")
    print(f"   📊 Daily Average: ₹{summary['daily_average']:,.0f}")
    print(f"   🏆 Top Category: {summary['top_category']['name']}")
    print(f"   {summary['trend']['message']}")
    
    # 6. Get remaining budget
    print("\n6️⃣ Budget remaining...")
    remaining = bm.get_remaining_budget(em.get_total_spent())
    print(f"   Monthly Budget: ₹{remaining['monthly_budget']:,.0f}")
    print(f"   Total Spent: ₹{remaining['total_spent']:,.0f}")
    print(f"   Remaining: ₹{remaining['remaining']:,.0f}")
    print(f"   Used: {remaining['percentage_used']:.1f}%")
    
    # 7. Saving tips
    print("\n7️⃣ Saving Tips:")
    tips = insights.get_savings_tips(spent)
    for tip in tips:
        print(f"   {tip}")
    
    print("\n" + "=" * 50)
    print("✅ INTEGRATION TEST PASSED!")
    print("=" * 50)

if __name__ == "__main__":
    run_integration_test()