//  Default Categories
export const DEFAULT_CATEGORIES: { name: string; icon: string; color: string }[] = [
  { name: 'Food', icon: '🍕', color: '#ef4444' },
  { name: 'Transport', icon: '🚗', color: '#f97316' },
  { name: 'Shopping', icon: '🛒', color: '#eab308' },
  { name: 'Entertainment', icon: '🎬', color: '#22c55e' },
  { name: 'Bills', icon: '📱', color: '#3b82f6' },
  { name: 'Health', icon: '💊', color: '#ec4899' },
  { name: 'Groceries', icon: '🥬', color: '#14b8a6' },
  { name: 'Education', icon: '📚', color: '#8b5cf6' },
  { name: 'Other', icon: '📦', color: '#6b7280' },
];

// App config
export const APP_CONFIG = {
    appName: 'CashCraft',
    version: '1.0.0',
    currency: '₹',
    currencyCode: 'INR',
};

// Date formats
export const DATE_FORMATS = {
    display: 'DD MMM YYYY',
    api: 'YYYY-MM-DD',
    monthYear: 'MMMM YYYY',
};