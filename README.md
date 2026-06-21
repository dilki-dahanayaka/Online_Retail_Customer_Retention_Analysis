# Online Retail Analytics Platform 📊🚀

## 1. Executive Summary

The **Online Retail Analytics Platform** is a data-driven Business Intelligence and Data Engineering solution designed to resolve critical visibility gaps within global e-commerce transactional operations.

This platform bridges the gap between raw transactional data and executive decision-making through:

- Python Data Cleaning
- Database Architecture & SQL Ingestion
- Exploratory Data Analysis
- RFM Customer Segmentation
- KPI Engineering
- Power BI Dashboarding
  

---

## 🛠 Technology Stack

* **Data Science & Engineering:** Python 3.x (Pandas, NumPy, Matplotlib, Seaborn)
* **Interactive Environment:** Jupyter Notebooks (Prototyping & EDA)
* **Business Intelligence:** Microsoft Power BI Desktop (Data Modeling, Custom DAX, UI/UX Design)
* **Segmentation Methodology:** Statistical RFM Modeling (Recency, Frequency, Monetary)
* **Database Management:** SQLite 3 Engine (Structured Relational Layer, Schema Normalization)

---

## 📂 Project Structure

```text
Online_Retail_Customer_Retention_Analysis/
│
├── dashboard/
│   ├── logo.png
│   ├── dashboard_preview.png
│   ├── OnlineRetailDashboard.pbix
│   └── OnlineRetailDashboard.pdf
│
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx         (Raw Multi-Country Source Dataset)
│   ├── database/
│   │   └── online_retail_warehouse.db (⚡ Engine-Generated SQLite Database File)
│   └── processed/
│       ├── cleaned_online_retail.csv
│       ├── country_summary.csv
│       ├── customer_segments.csv
│       ├── customer_summary.csv
│       ├── kpi_summary.csv
│       └── product_summary.csv
│
├── images/
│   ├── correlation_heatmap.png
│   ├── customer_segments.png
│   ├── monthly_revenue.png
│   ├── revenue_distribution.png
│   ├── top_countries.png
│   ├── top_customers.png
│   └── top_products.png
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_RFM_Analysis.ipynb
│   ├── 05_KPI_Calculation.ipynb
│   └── 06_Final_Insights.ipynb
│
├── src/
│   ├── db_ingestion.py                (⚡ SQL Schema Creation & Data Loading Engine)
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── rfm_analysis.py
│   ├── kpi_calculation.py
│   └── visualization.py
│
├── main.py                            (Unified Pipeline Executive Coordinator)
├── queries.sql                        (⚡ University Assignment Mandatory SQL Scripts)
├── requirements.txt
└── README.md
```
---

## 🗄️ Relational Database Architecture & SQL Ingestion

To satisfy strict data integrity guidelines and simulate an enterprise data warehouse environment, the system utilizes a local SQLite database engine. Instead of conducting flat-file manipulation, the raw operational rows are split into two distinct, normalized relational database tables.

```text
   [transaction_records]                       [customer_registry]
   ---------------------                       -------------------
   - InvoiceNo (TEXT)                          - CustomerID (TEXT) <---+ [PK]
   - StockCode (TEXT)                          - Country (TEXT)        |
   - Description (TEXT)                                                |
   - Quantity (INTEGER)                                                | (INNER JOIN)
   - InvoiceDate (TEXT)                                                |
   - UnitPrice (REAL)                                                  |
   - CustomerID (TEXT) ------------------------------------------------+ [FK]
```
---
## 🧹 Applied Data Cleansing Framework

To ensure data quality and eliminate analytical bias, the raw online retail dataset containing over 500,000 international transactions was processed through a structured data cleaning pipeline.

### ✔ Cancellation Filtering
Transactions with negative quantities or values (representing cancellations and returns) were removed to ensure accurate revenue calculations.

### ✔ Missing Customer ID Removal
Records without a valid `CustomerID` were excluded to maintain reliable customer-level analysis and segmentation.

### ✔ Revenue Calculation

Revenue was calculated for each transaction using:

```python
Revenue = Quantity × UnitPrice
```

This formula was applied consistently across the dataset to generate accurate financial metrics.

### ✔ RFM Customer Segmentation

Customers were classified according to their:

- **Recency** – How recently they made a purchase.
- **Frequency** – How often they purchased.
- **Monetary Value** – How much revenue they generated.

The segmentation process was implemented programmatically using the `rfm_analysis.py` module, enabling the identification of high-value customer groups and potential churn risks.

---

### 🔄 Data Processing Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
RFM Segmentation
     ↓
KPI Calculation
     ↓
Visualization
     ↓
Power BI Dashboard
```
## 📊 Dashboard Preview

<img width="873" height="489" alt="dashboard" src="https://github.com/user-attachments/assets/37dc31aa-89d2-4999-8c14-78ebd14f9438" />



---

# Dashboard Metrics & Key Findings

The Power BI dashboard provides insights into customer behavior, product performance, geographical sales distribution, and seasonal trends. The analysis reveals several strategic realities that directly influence business performance.

---

## 🔹 High Customer Revenue Concentration

- Total Revenue: **$8.91M**
- Active Customers: **4,338**
- Revenue is highly concentrated among a small group of high-value customers.

### Key Insight
The **Top 10 Customers by Revenue** and **Champion Segment** indicate that a limited number of wholesale clients generate a substantial portion of total sales.

### Business Recommendation
Implement a **VIP Customer Retention Program** to minimize churn risk and protect revenue streams.

---

## 🌍 Geographic Revenue Imbalance

### Key Insight

The **United Kingdom** contributes more than 90% of total revenue, while countries such as Spain, Sweden, and Switzerland contribute significantly less.

### Business Risk

Heavy dependence on a single market exposes the business to economic and regulatory risks.

### Business Recommendation

Expand international wholesale channels through targeted regional marketing campaigns and market diversification strategies.

---

## 📦 Product Revenue Concentration

### Key Insight

A small number of products dominate overall sales performance.

Among them, **PAPER CRAFT** generates approximately **$0.17M** in revenue.

### Business Recommendation

- Prioritize inventory availability for top-performing products.
- Reduce holding costs by managing low-performing inventory efficiently.
- Maintain zero stock-outs for high-demand items.

---

## 📅 Revenue Seasonality

### Key Insight

The Monthly Revenue Trend reveals a strong upward trend during **Q4**, driven by holiday-season demand.

### Business Recommendation

- Increase inventory levels before peak demand periods.
- Improve logistics planning and shipping capacity.
- Prepare procurement schedules ahead of the holiday season.

---

# 📊 Dashboard Metrics

✔ Total Revenue

✔ Top 10 Customers by Revenue

✔ Revenue by Country

✔ Top Products

✔ Monthly Revenue Trend

✔ Customer Segmentation (RFM)

✔ KPI Summary

---

# 🎯 Strategic Outcomes

- Improve customer retention and reduce churn.
- Optimize inventory allocation.
- Diversify geographic revenue streams.
- Prepare proactively for seasonal demand fluctuations.

---
## 🏆 Final Analytical Insights Matrix (Project Outputs)

The following structured performance matrix summarizes the core financial discoveries, business realities, and operational interventions derived from the data analysis pipeline:

| Analytical Pillar | Key Performance Metrics | Empirical Finding & Discovery | Strategic Business Action |
| :--- | :--- | :--- | :--- |
| **Enterprise Growth** | <ul><li>Total Revenue: **$8.91M**</li><li>Active Customers: **4,338**</li><li>Total Orders: **18,532**</li><li>Avg Order Line: **$22.40**</li></ul> | The retail business has a strong market footprint but experiences structural vulnerabilities across segment dependencies. | Transition from broad customer acquisition to high-value client retention modeling. |
| **Customer Profiling** | <ul><li>Elite Segment: **Champions**</li><li>Risk Profile: **High Concentration**</li></ul> | Revenue is heavily concentrated within a small group of high-volume wholesale corporate accounts. | Implement a dedicated **VIP Customer Retention Program** to minimize churn risk. |
| **Geographic Density** | <ul><li>UK Revenue Share: **>90%**</li><li>Global Outliers: **Spain, Sweden**</li></ul> | Extreme dependency on the United Kingdom domestic market, creating an exposure to localized economic shocks. | Expand international wholesale channels via **Targeted Regional Marketing Campaigns**. |
| **Inventory Portfolio** | <ul><li>Top Performer: **PAPER CRAFT**</li><li>Asset Revenue: **~$0.17M**</li></ul> | Portfolio monetization is highly top-heavy; a minor subset of specialized seasonal SKUs drive core cash flow. | Prioritize supply chain pathways to ensure **Zero Stockouts** for high-performing product assets. |
| **Temporal Demand** | <ul><li>Peak Vector: **Q4 (Holiday)**</li><li>Buying Model: **Seasonal Cycles**</li></ul> | Clear revenue acceleration during Q4, heavily driven by holiday-season B2B wholesale procurement. | Restructure procurement schedules and scale logistics capacity months prior to peak Q4 demand. |
