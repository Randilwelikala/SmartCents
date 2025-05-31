import streamlit as st;

def give_savings_advice(income, expenses_df):
    total_spent = expenses_df['Amount'].sum()
    category_spending = expenses_df.groupby('Category')['Amount'].sum()
    
    

    if total_spent > income:
        st.write("- You're spending more than your income. Urgent action needed!")

    for category, amount in category_spending.items():
        percent = (amount / income) * 100
        if percent > 15:
            st.write(f"- Try to reduce spending on {category} (currently {percent:.1f}% of income).")

    if (income - total_spent) < 100:
        st.write("- Your savings are below LKR 100. Try to save at least 10% of your income.")
    else:
        st.write("- Good job! Your savings are on track.")
