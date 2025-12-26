import { create } from "zustand";
import { supabase } from "../services/supabaseClient";
import { Expense, Category, DashboardSummary } from "../types";
import { getCurrentMonthYear } from "../utils/formatters";

interface ExpenseState {
  expenses: Expense[];
  categories: Category[];
  isLoading: boolean;
  error: string | null;

  // Actions
  fetchExpenses: (month?: number, year?: number) => Promise<void>;
  fetchCategories: () => Promise<void>;
  addExpense: (
    expense: Omit<Expense, "id" | "created_at">
  ) => Promise<{ error: Error | null }>;
  deleteExpense: (id: string) => Promise<{ error: Error | null }>;
  getDashboardSummary: () => DashboardSummary;
}

export const useExpenseStore = create<ExpenseState>((set, get) => ({
  expenses: [],
  categories: [],
  isLoading: false,
  error: null,

  fetchExpenses: async (month?: number, year?: number) => {
    set({ isLoading: true, error: null });

    try {
      const { month: currentMonth, year: currentYear } = getCurrentMonthYear();
      const targetMonth = month ?? currentMonth;
      const targetYear = year ?? currentYear;

      // Create date range for the month
      const startDate = new Date(targetYear, targetMonth - 1, 1);
      const endDate = new Date(targetYear, targetMonth, 0);

      const { data, error } = await supabase
        .from("expenses")
        .select(
          `
          *,
          category:categories(*)
        `
        )
        .gte("date", startDate.toISOString().split("T")[0])
        .lte("date", endDate.toISOString().split("T")[0])
        .order("date", { ascending: false });

      if (error) throw error;

      set({ expenses: data || [], isLoading: false });
    } catch (error) {
      set({ error: (error as Error).message, isLoading: false });
    }
  },

  fetchCategories: async () => {
    try {
      const { data, error } = await supabase
        .from("categories")
        .select("*")
        .order("name");

      if (error) throw error;

      set({ categories: data || [] });
    } catch (error) {
      console.error("Error fetching categories:", error);
    }
  },

  addExpense: async (expense) => {
    try {
      const { error } = await supabase.from("expenses").insert([expense]);

      if (error) throw error;

      // Refresh expenses
      await get().fetchExpenses();

      return { error: null };
    } catch (error) {
      return { error: error as Error };
    }
  },

  deleteExpense: async (id: string) => {
    try {
      const { error } = await supabase.from("expenses").delete().eq("id", id);

      if (error) throw error;

      // Update local state
      set({ expenses: get().expenses.filter((e) => e.id !== id) });

      return { error: null };
    } catch (error) {
      return { error: error as Error };
    }
  },

  getDashboardSummary: () => {
    const { expenses, categories } = get();

    const totalSpent = expenses.reduce((sum, e) => sum + Number(e.amount), 0);

    const categoryTotals: Record<string, number> = {};
    expenses.forEach((expense) => {
      const categoryName = expense.category?.name || "Other";
      categoryTotals[categoryName] =
        (categoryTotals[categoryName] || 0) + Number(expense.amount);
    });

    return {
      totalSpent,
      totalExpenses: expenses.length,
      monthlyBudget: 0, // Will be set from budget store
      remaining: 0,
      percentageUsed: 0,
      categoryTotals,
      recentExpenses: expenses.slice(0, 5),
    };
  },
}));
