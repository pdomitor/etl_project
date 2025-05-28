-- 3. Crear tabla destino si no existe
CREATE TABLE IF NOT EXISTS daily_revenue_jan2025 (
    sku_id TEXT,
    date_id DATE,
    price REAL,
    sales INTEGER DEFAULT 0,
    revenue REAL DEFAULT 0,
    PRIMARY KEY (sku_id, date_id)
);