def give_savings_advice(income, expenses_df):
    total_spent = expenses_df['Amount'].sum()
    category_spending = expenses_df.groupby('Category')['Amount'].sum()
    
    print("\n--- Personalized Advice ---")

    if total_spent > income:
        print("You're spending more than your income. Urgent action needed!")

    for category, amount in category_spending.items():
        percent = (amount / income) * 100
        if percent > 15:
            print(f"Try to reduce spending on {category} (currently {percent:.1f}% of income).")

    if (income - total_spent) < 100:
        print("Your savings are below $100. Try to save at least 10% of your income.")
    else:
        print("Good job! Your savings are on track.")
