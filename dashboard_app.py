import streamlit as st
import pandas as pd
from visualizer import plot_expenses_by_category

df = pd.read_csv('expenses.csv')
df['Date'] = pd.to_datetime(df['Date'])

st.title("AI Finance Tracker")
st.write("## Expense Overview")
st.dataframe(df)

if st.button("Show Pie Chart"):
    plot_expenses_by_category(df[df['Category'] != 'Income'])
