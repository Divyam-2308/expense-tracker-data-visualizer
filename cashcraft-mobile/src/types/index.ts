// User type
export interface User {
    id: string;
    email: string;
    name: string;
    avatar_url?: string;
    created_at: string;
}

// Category type
export interface Category {
    id: string;
    name: string;
    icon: string;
    color: string;
    is_default: boolean;
    user_id: string;
}

//Expense type
export interface Expense {
    id: string;
    user_id: string;
    category_id: string;
    category?: Category;
    amount: number;
    description?: string;
    merchant?: string;
    date: string;
    source: 'manual' | 'sms' | 'notification';
    raw_message?: string;
    created_at: string;
}

// Budget type
export interface Budget {
    id: string;
    user_id: string;
    category_id: string;
    category?: Category;
    amount: number;
    month: number;
    year: number;
    spent?: number;
}

// Parsed SMS type
export interface ParsedTransaction {
    amount: number;
    merchant: string | null;
    type: 'debit' | 'credit';
    bank: string | null;
    upiRef: string | null;
    rawMessage: string;
}

// Dashboard Summary type
export interface DashboardSummary {
    totalExpenses: number;
    monthlyBudget: number;
    remaining: number;
    percentageUsed: number;
    categoryTotals: Record<string, number>;
    recentExpenses: Expense[];
}