import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_expenses_by_category(expense_df):
    category_totals = expense_df.groupby('Category')['Amount'].sum()
    
    fig, ax = plt.subplots()
    category_totals.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    
    ax.set_title('Expenses by Category')
    ax.set_ylabel('')
    
    st.pyplot(fig)  # ✅ Show the plot in Streamlit

def plot_expenses_over_time(expense_df):
    df_daily = expense_df.groupby('Date')['Amount'].sum()
    
    fig, ax = plt.subplots()
    df_daily.plot(kind='line', marker='o', ax=ax)
    
    ax.set_title('Daily Expenses Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount')
    ax.grid(True)
    
    st.pyplot(fig)  # ✅ Show the plot in Streamlit
