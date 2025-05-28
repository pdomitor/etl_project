-- 5. Insertar los datos combinados
INSERT INTO daily_revenue_jan2025 (sku_id, date_id, price, sales, revenue)
SELECT 
    p.sku_id,
    c.date_id,
    p.price,
    COALESCE(s.total_sales, 0) AS sales,
    COALESCE(s.total_sales, 0) * p.price AS revenue
FROM 
    product p
CROSS JOIN 
    calendar c
LEFT JOIN (
    SELECT 
        sku_id,
        DATE(orderdate_utc) AS date_id,
        SUM(sales) AS total_sales
    FROM sales
    WHERE DATE(orderdate_utc) BETWEEN '2025-01-01' AND '2025-01-31'
    GROUP BY sku_id, DATE(orderdate_utc)
) s
ON p.sku_id = s.sku_id AND c.date_id = s.date_id;
