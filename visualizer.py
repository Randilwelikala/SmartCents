import matplotlib.pyplot as plt
import seaborn as sns

def plot_expenses_by_category(expense_df):
    category_totals = expense_df.groupby('Category')['Amount'].sum()
    category_totals.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expenses by Category')
    plt.ylabel('')
    plt.show()

def plot_expenses_over_time(expense_df):
    df_daily = expense_df.groupby('Date')['Amount'].sum()
    df_daily.plot(kind='line', marker='o')
    plt.title('Daily Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.show()
