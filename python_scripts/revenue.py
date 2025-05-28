import logging
import pandas as pd
from python_scripts.db import get_connection, create_table_if_not_exists, log_etl_run
from python_scripts.data_processing import (
    load_products, load_sales, create_date_range,
    generate_all_combinations, merge_sales_data
)
from python_scripts.config import DB_PATH, START_DATE, END_DATE

logger = logging.getLogger(__name__)

def insert_daily_revenue(conn, daily_revenue: pd.DataFrame):
    logger.info("Inserting daily revenue data into database (replace mode)...")
    daily_revenue.to_sql('daily_revenue_jan2025', conn, if_exists='replace', index=False)

def generate_daily_revenue_jan2025(db_path: str = DB_PATH,
                                   start_date: str = START_DATE,
                                   end_date: str = END_DATE):
    logger.info("Starting daily revenue generation process...")
    with get_connection(db_path) as conn:
        products = load_products(conn)
        sales = load_sales(conn, start_date, end_date)
        dates = create_date_range(start_date, end_date)
        all_combinations = generate_all_combinations(products, dates)
        daily_revenue = merge_sales_data(all_combinations, sales)
        
        create_table_if_not_exists(conn)
        insert_daily_revenue(conn, daily_revenue)
        log_etl_run(conn)  # ← log ETL run here

        # Log summary
        result_count = len(daily_revenue)
        logger.info(f"Daily revenue data generated with {result_count} rows.")
        print(daily_revenue)
