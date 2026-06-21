
-- 1. BASIC SELECT & WHERE CLAUSE
SELECT InvoiceNo, StockCode, Description, Quantity, UnitPrice, CustomerID 
FROM transaction_records
WHERE Quantity > 0 AND UnitPrice > 0
LIMIT 10;


-- 2. INNER JOIN OPERATION
SELECT t.InvoiceNo, t.StockCode, t.Description, t.Quantity, t.UnitPrice, t.CustomerID, c.Country
FROM transaction_records t
INNER JOIN customer_registry c 
    ON t.CustomerID = c.CustomerID
LIMIT 10;


-- 3. GROUP BY & AGGREGATE FUNCTIONS
SELECT 
    t.InvoiceNo, 
    t.StockCode, 
    t.Description, 
    SUM(t.Quantity) AS Total_Quantity, 
    t.InvoiceDate, 
    AVG(t.UnitPrice) AS UnitPrice, 
    t.CustomerID, 
    c.Country
FROM transaction_records t
INNER JOIN customer_registry c 
    ON t.CustomerID = c.CustomerID
GROUP BY 
    t.InvoiceNo, 
    t.StockCode, 
    t.Description, 
    t.InvoiceDate, 
    t.CustomerID, 
    c.Country;


-- 4. GROUP BY & HAVING CLAUSE
SELECT c.Country, COUNT(t.InvoiceNo) AS Total_Orders
FROM transaction_records t
INNER JOIN customer_registry c 
    ON t.CustomerID = c.CustomerID
GROUP BY c.Country
HAVING COUNT(t.InvoiceNo) > 100
ORDER BY Total_Orders DESC;