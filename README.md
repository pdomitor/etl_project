# Daily Revenue Generator for January 2025

This script calculates daily revenue per product for January 2025 from a SQLite database and stores the result in a new table.

---

## Prerequisites

- Python 3
- SQLite

---

## Python + cron Implementation

### Project Structure

```
etl_project/
├── python_scripts/                     # Python Dependencies
│   ├── config.py                       # Variables definition
│   ├── data_processing.py              # ETL Toolkit
│   ├── db.py                           # Connection & DDL
│   ├── revenue.py                      # Main script
├── data/                              
│   └── product_sales.db                # SQLite database
├── logs/
│   └── etl_YYYYMMDD.log                # Execution logs
├── utils/                              
│   └── profiling.py                    # Exploratory Data Analysis
├── run.py                              # Entry script
├── setup.py                            # Python setup
├── requirements.txt                    # Python libraries
└── README.md                           # Short description of the project
```

### Usage

#### For data exploratory analysis
```bash
python utils/profiling.py
```

#### How to Run Manually
```bash
python run.py
```

#### How to Schedule with cron

Edit your crontab:
```bash
crontab -e
```

Add the following line to run the ETL monthly at 3 AM on the 1st:
```bash
0 3 1 * * /path/to/etl_project/run.py
```

---

## SQL + Bash + cron Implementation

### Project Structure

```
etl_project/
├── sql_scripts/                        # SQL scripts (self-explanatory)
│   ├── 00_clean.sql                        
│   ├── 01_create_calendar.sql
│   ├── 02_insert_calendar.sql
│   ├── 03_create_daily_revenue_table.sql
│   ├── 04_clear_daily_revenue_table.sql
│   ├── 05_insert_daily_revenue_data.sql
│   └── 06_audit_logging.sql
├── data/                              
│   └── product_sales.db                # SQLite database
├── logs/
│   └── etl_YYYYMMDD.log                # Execution logs
├── run_etl.sh                          # Bash script to run ETL steps
└── README.md                           # Short description of the project
```

### Usage

#### How to Run Manually
```bash
./run_etl.sh
```

#### How to Schedule with cron

Edit your crontab:
```bash
crontab -e
```

Add the following line to run the ETL monthly at 2 AM on the 1st:
```bash
0 2 1 * * /path/to/etl_project/run_etl.sh
```

#### How to access sqlite3

Open the SQLite database:
```bash
sqlite3 data/product_sales.db
```

Once inside:
```sql
.tables    -- List tables
```