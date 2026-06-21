import pandas as pd

def add_features(df):
    print(" Feuture Engineering start...")
    # Total Revenue 
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    
    # time and data devided
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    
    return df