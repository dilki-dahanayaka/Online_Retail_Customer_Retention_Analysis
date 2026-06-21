import os
import sqlite3
import pandas as pd

def ingest_data_to_sql(raw_excel_path, db_path):
    """
    Reads the raw Excel dataset, splits it into two normalized relational tables,
    and writes them into a local SQLite database engine to allow JOIN operations.
    """
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    print("SQL Database layer initializing...")
    conn = sqlite3.connect(db_path)
    
    print("Loading raw Excel data into memory...")
    df = pd.read_excel(raw_excel_path, engine='openpyxl')
    
    # Normalizing into Table 1: Transaction Records (Without Country column)
    df_transactions = df[['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID']].copy()
    
    # Normalizing into Table 2: Customer Registry (Mapping CustomerID to Country)
    df_customers = df[['CustomerID', 'Country']].drop_duplicates().dropna(subset=['CustomerID']).copy()
    
    print("Generating Relational Tables within SQLite Engine...")
    df_transactions.to_sql('transaction_records', conn, if_exists='replace', index=False)
    df_customers.to_sql('customer_registry', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Success: Relational Tables ('transaction_records' & 'customer_registry') successfully injected!\n")