import pandas as pd

def perform_rfm_analysis(df):
    print("RFM Analysis starting..")
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    
    # RFM Core Values ​​Search
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
        'InvoiceNo': 'nunique',                                  # Frequency
        'TotalRevenue': 'sum'                                    # Monetary
    }).reset_index()
    
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    
    # Giving scores from 1-5
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop')
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
    
    # Customer Segmentation Logic 
    def assign_segment(row):
        r, f, m = int(row['R_Score']), int(row['F_Score']), int(row['M_Score'])
        if r >= 4 and f >= 4 and m >= 4:
            return 'High-Value / Champions'
        elif r <= 2 and f >= 3 and m >= 3:
            return 'At Risk / Can\'t Lose Them'
        elif r <= 2 and f <= 2 and m <= 2:
            return 'Lost / Hibernating'
        else:
            return 'Average/Potential Loyalists'
            
    rfm['Customer_Segment'] = rfm.apply(assign_segment, axis=1)
    print("RFM Segmentation conplete !")
    return rfm