import os

DB_PATH = os.getenv('DB_PATH', 'data/product_sales.db')
START_DATE = os.getenv('START_DATE', '2025-01-01')
END_DATE = os.getenv('END_DATE', '2025-01-31')
