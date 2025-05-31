import streamlit as st
import pandas as pd
from visualizer import plot_expenses_by_category, plot_expenses_over_time
from advisor import give_savings_advice
from forecast import forecast_expenses

# Load data
df = pd.read_csv('expenses.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Separate income and expenses
income_df = df[df['Category'] == 'Income']
expense_df = df[df['Category'] != 'Income']

total_income = income_df['Amount'].sum()
total_expense = expense_df['Amount'].sum()
savings = total_income - total_expense

st.title("SmartCents")

st.write(" ## Expense Overview")
st.dataframe(df)

st.write(f"**Total Income:** LKR {total_income}")
st.write(f"**Total Expenses:** LKR {total_expense}")
st.write(f"**Total Savings:** LKR {savings}")

if st.button(" Show Pie Chart"):
    plot_expenses_by_category(expense_df)

if st.button(" Show Line Chart"):
    plot_expenses_over_time(expense_df)

if st.button(" Show Forecast"):
    forecast = forecast_expenses(expense_df)
    st.success(forecast)

if st.button(" Get Financial Advice"):
    st.write("Check terminal for advice.")
    give_savings_advice(total_income, expense_df)
