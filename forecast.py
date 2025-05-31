from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_expenses(expense_df):
    df = expense_df.copy()
    df['Day'] = df['Date'].dt.day
    X = df[['Day']]
    y = df['Amount']
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_day = [[max(df['Day']) + 1]]
    prediction = model.predict(future_day)
    
    return f"Predicted expense for day {future_day[0][0]}: ${prediction[0]:.2f}"
