import pandas as pd

def calculate_business_kpis(df, rfm_df):
    print("KPIs calculation has starting...")
    kpis = {}
    
    kpis['Total_Revenue'] = df['TotalRevenue'].sum()
    kpis['Total_Orders'] = df['InvoiceNo'].nunique()
    kpis['Total_Customers'] = rfm_df['CustomerID'].nunique()
    kpis['Average_Order_Value'] = kpis['Total_Revenue'] / kpis['Total_Orders']
    
    # Retention Rate (active customers / Total Customers)
    active_customers = rfm_df[rfm_df['Recency'] <= 90]['CustomerID'].nunique()
    kpis['Retention_Rate_90D'] = (active_customers / kpis['Total_Customers']) * 100
    
    return kpis