import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    print(" Data Cleaning start...")
   
    # Excel or CSV read
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
       
        df = pd.read_excel(file_path, engine='openpyxl')
    else:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        
    print(f" Data read complete! Total number of rows: {len(df):,}")
    print(" Removing Missing Values ​​and Cancelled Orders")
    
    # removing Missing Customer IDs
    df = df.dropna(subset=['CustomerID'])
    
    # removing Cancelled Orders
    df['InvoiceNo'] = df['InvoiceNo'].astype(str)
    df = df[~df['InvoiceNo'].str.startswith('C', na=False)]
    df = df[df['Quantity'] > 0]
    
    # Removing incorrect prices
    df = df[df['UnitPrice'] > 0]
    
    # Data Types
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int).astype(str)
    
    print(f"Data Cleaning Completed. Number of Cleaned Data Rows: {len(df):,}")
    return df