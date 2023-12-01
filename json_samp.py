import streamlit as st
import pandas as pd

# Sample DataFrame

sample_data = 'Data1.xlsx'
sample_data1=pd.read_excel(sample_data)

sample_data1['Date'] = pd.to_datetime(sample_data1['Date'])

# Group by 'Customer_ID', 'Account_ID', and 'Date'
grouped_df = sample_data1.groupby(['Customer_ID', 'Account_ID', 'Date', 'Account_Type', 'Transaction_Type']).agg({
    'Amount': 'sum',
    'Trn_Count': 'sum'
}).reset_index()

# Create the desired JSON structure
# Create the desired JSON structure
grouped_df['Features'] = grouped_df.apply(lambda row: {
    'amount': {
        'trading': row['Amount'] if row['Transaction_Type'] == 'Trading' else 0,
        'deposit': row['Amount'] if row['Transaction_Type'] == 'Deposit' else 0
    },
    'trn_count': {
        'trading': row['Trn_Count'] if row['Transaction_Type'] == 'Trading' else 0,
        'deposit': row['Trn_Count'] if row['Transaction_Type'] == 'Deposit' else 0
    }
}, axis=1)
# Drop unnecessary columns
grouped_df.drop(['Amount', 'Trn_Count', 'Account_Type', 'Transaction_Type'], axis=1, inplace=True)

# Dropdown to select columns
selected_column = grouped_df.selectbox('Select a column:', grouped_df.columns)

# Display the selected column
st.write(f"Selected column: {selected_column}")
st.write(df[selected_column])
