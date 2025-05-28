import sqlite3
import logging

logger = logging.getLogger(__name__)

def get_connection(db_path: str):
    return sqlite3.connect(db_path)

def create_table_if_not_exists(conn):
    logger.info("Creating table daily_revenue_jan2025 if not exists...")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS daily_revenue_jan2025 (
            sku_id TEXT,
            date_id DATE,
            price REAL,
            sales INTEGER,
            revenue REAL,
            PRIMARY KEY (sku_id, date_id)
        )
    """)
    logging.info("Logging ETL run to etl_log table...")

def log_etl_run(conn):
    # Create log table if not exists
    conn.execute("""
        CREATE TABLE IF NOT EXISTS etl_log (
            run_time TEXT,
            rows_inserted INTEGER
        )
    """)
    conn.commit()

    # Insert log entry with current time and row count
    conn.execute("""
        INSERT INTO etl_log (run_time, rows_inserted)
        VALUES (
            datetime('now'),
            (SELECT COUNT(*) FROM daily_revenue_jan2025)
        )
    """)


    conn.commit()
