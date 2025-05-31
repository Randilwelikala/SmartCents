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

st.write("##  Add New Expense or Income")

with st.form("entry_form", clear_on_submit=True):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Subscriptions", "Income", "Other"])
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("Add Entry")

if submitted:
    new_entry = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }])

    # Append to CSV
    new_entry.to_csv("expenses.csv", mode='a', header=False, index=False)
    st.success("✅ Entry added successfully!")

    # Refresh data by re-running script (optional)
    st.rerun()


st.write(" ## Expense Overview")
st.dataframe(df)

st.write(f"**Total Income  :** LKR {total_income:.2f}")
st.write(f"**Total Expenses  :** LKR {total_expense:.2f}")
st.write(f"**Total Savings  :** LKR {savings:.2f}")

if st.button(" Show Pie Chart"):
    plot_expenses_by_category(expense_df)

if st.button(" Show Line Chart"):
    plot_expenses_over_time(expense_df)

if st.button(" Show Forecast"):
    forecast = forecast_expenses(expense_df)
    st.success(forecast)

if st.button(" Get Financial Advice"):    
    give_savings_advice(total_income, expense_df)
