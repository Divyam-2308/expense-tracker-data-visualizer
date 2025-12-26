/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./App.{js,jsx,ts,tsx}",
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    presets: [require('nativewind/preset')],
    theme: {
        extend: {
            colors: {
                primary: {
                    50: '#f0fdf4',
                    100: '#dcfce7',
                    500: '#22c55e',
                    600: '#16a34a',
                    700: '#15803d',
                },
                secondary: {
                    500: '#6366f1',
                    600: '#4f46e5',
                },
                background: '#f8fafc',
                card: '#ffffff',
                text: {
                    primary: '#1e293b',
                    secondary: '#64748b',
                }
            }
        },
    },
    plugins: [],
};
