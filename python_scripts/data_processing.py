import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_products(conn) -> pd.DataFrame:
    logger.info("Loading products data...")
    return pd.read_sql("SELECT sku_id, price FROM product", conn)

def load_sales(conn, start_date: str, end_date: str) -> pd.DataFrame:
    logger.info(f"Loading sales data from {start_date} to {end_date}...")
    query = f"""
        SELECT sku_id, DATE(orderdate_utc) AS date_id, SUM(sales) AS sales
        FROM sales
        WHERE DATE(orderdate_utc) BETWEEN ? AND ?
        GROUP BY sku_id, DATE(orderdate_utc)
    """
    return pd.read_sql(query, conn, params=(start_date, end_date), parse_dates=["date_id"])

def create_date_range(start_date: str, end_date: str) -> pd.DataFrame:
    logger.info(f"Creating date range from {start_date} to {end_date}...")
    dates = pd.date_range(start_date, end_date)
    return pd.DataFrame({'date_id': dates})

def generate_all_combinations(products: pd.DataFrame, dates: pd.DataFrame) -> pd.DataFrame:
    logger.info("Generating all product-date combinations...")
    products = products.copy()
    dates = dates.copy()
    products['key'] = 1
    dates['key'] = 1
    combined = pd.merge(products, dates, on='key').drop(columns='key')
    return combined

def merge_sales_data(all_combinations: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    logger.info("Merging sales data with all combinations...")
    merged = pd.merge(all_combinations, sales, on=['sku_id', 'date_id'], how='left')
    merged['sales'] = merged['sales'].fillna(0).astype(int)
    merged['revenue'] = merged['price'] * merged['sales']
    return merged[['sku_id', 'date_id', 'price', 'sales', 'revenue']]
