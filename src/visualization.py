import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_and_save_plots(df, rfm_df, output_dir="images"):
    os.makedirs(output_dir, exist_ok=True)
   
    
    # 1. Customer Segments Distribution
    plt.figure(figsize=(10, 5))
    sns.countplot(y='Customer_Segment', data=rfm_df, palette='viridis', order=rfm_df['Customer_Segment'].value_counts().index)
    plt.title('Customer Segments Distribution')
    plt.xlabel('Number of Customers')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'customer_segments.png'))
    plt.close()
    
    # 2. Monthly Revenue Trend
    monthly_rev = df.groupby('InvoiceMonth')['TotalRevenue'].sum().reset_index()
    monthly_rev['InvoiceMonth'] = monthly_rev['InvoiceMonth'].astype(str)
    plt.figure(figsize=(12, 5))
    plt.plot(monthly_rev['InvoiceMonth'], monthly_rev['TotalRevenue'], marker='o', color='b', linestyle='-')
    plt.title('Monthly Revenue Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'revenue_trend.png'))
    plt.close()
    
    print("All graphs are saved in the 'images/' folder.!")