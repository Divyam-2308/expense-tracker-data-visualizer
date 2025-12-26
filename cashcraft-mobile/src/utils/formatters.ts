import { APP_CONFIG } from "../constants";

/**
 * Formats a number as a currency string.
 */

export function formatCurrency(amount: number): string{
    return `${APP_CONFIG.currency}${amount.toLocaleString('en-IN', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 2,
    })}`;
}

/**
 * Formats a date string to a more readable format.
 */
export function formatDate(date: string | Date): string {
    const d = new Date(date);
    return d.toLocaleDateString('en-IN', {
        day: '2-digit',
        month: 'short',
        year: 'numeric',
    });
}

/**
 * Format date to relative time (e.g., "2 days ago").
 */
export function formatRelativeDate(date: string | Date): string {
    const d = new Date(date);
    const today = new Date(date);
    const yesterday = new Date(today);
    yesterday.setDate(today.getDate() - 1);

    if (d.toDateString() === today.toDateString()) {
        return 'Today';
    } else if (d.toDateString() === yesterday.toDateString()) {
        return 'Yesterday';
    } else {
        return formatDate(d);
    }
}

/**
 * Get current month and year
 */
export function getCurrentMonthYear(): { month: number; year: number } {
    const now = new Date();
    return {
        month: now.getMonth() + 1,
        year: now.getFullYear(),
    };
}

/**
 * Calculate percentage
 */
export function calculatePercentage(value: number, total: number): number {
  if (total === 0) return 0;
  return Math.min(Math.round((value / total) * 100), 100);
}