# Daily Revenue Generator for January 2025

This script calculates daily revenue per product for January 2025 from a SQLite database and stores the result in a new table.

#Prerequisites
Python3
Sqlite

#Project Structure

#Python+cron Implementation

etl_project/
├── python_scripts/
│   ├── config.py
│   ├── data_processing.py
│   ├── db.py
│   ├── revenue.py
├── data/                  
│   ├── product_sales.db    # SQLite database
├── utils/
│   ├── profiling.py
├── run.py               # Entry script
├── setup.py     # Dependencies
├── requirements.txt     
└── README.md
	
## Usage

### For data exploratory analysis
python utils/profiling.py

###How to Run Manually
python run.py

###How to Schedule with cron
Edit your crontab:
crontab -e
Add the following line to run the ETL monthly at 3 AM on the 1st:
0 3 1 * * /path/to/etl_project/run.py

#SQL + Bash + cron Implementation

#Project Structure

etl_project/
├── sql_scripts/
│   ├── 00_clean.sql
│   ├── 01_create_calendar.sql
│   ├── 02_insert_calendar.sql
│   ├── 03_create_daily_revenue_table.sql
│   ├── 04_clear_daily_revenue_table.sql
│   ├── 05_insert_daily_revenue_data.sql
│   └── 06_audit_logging.sql
├── data/                  
│   ├── product_sales.db    # SQLite database
│── logs/
│    └── etl_YYYYMMDD.log   # Execution logs
├── run_etl.sh             # Bash script to run ETL steps
└── README.md

## Usage
###How to Run Manually

./run_etl.sh
cat logs/etl_$(date +%Y%m%d).log

###How to Schedule with cron
Edit your crontab:
crontab -e
Add the following line to run the ETL monthly at 2 AM on the 1st:
0 2 1 * * /path/to/etl_project/run_etl.sh


###How to access sqlite3

sqlite3 data/product_sales.db
Access the db

.tables
List tables
