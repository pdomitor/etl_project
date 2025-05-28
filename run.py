import logging
from datetime import datetime
from python_scripts.revenue import generate_daily_revenue_jan2025

def setup_logging():
    log_filename = f"logs/etl_{datetime.now().strftime('%Y%m%d')}.log"
    # Configure logging
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode='a'),
        logging.StreamHandler()  # console output
    ]
    )
def main():
    setup_logging()
    generate_daily_revenue_jan2025()

if __name__ == "__main__":
    main()
