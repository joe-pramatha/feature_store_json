import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    'Customer_ID': [1, 1, 2, 2, 3],
    'Account_ID': ['A123', 'A123', 'B456', 'B456', 'C789'],
    'Account_Type': ['Savings', 'Savings', 'Checking', 'Checking', 'Savings'],
    'Transaction_Type': ['Deposit', 'Withdrawal', 'Deposit', 'Withdrawal', 'Deposit'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'Amount': [100, 50, 200, 100, 150],
    'Trn_Count': [1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Create JSON columns dynamically
json_columns = ['JSON_Column_1', 'JSON_Column_2']  # Replace with your actual JSON column names
for col in json_columns:
    df[col] = df.apply(lambda row: f'{{"amount": {row["Amount"]}, "trn_count": {row["Trn_Count"]}}}', axis=1)

# Dropdown to select columns
selected_column = st.selectbox('Select a column:', df.columns)

# Display the selected column
st.write(f"Selected column: {selected_column}")
st.write(df[selected_column])
