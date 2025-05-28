#!/bin/bash

DB_PATH="data/product_sales.db"
SQL_DIR="sql_scripts"
LOG_FILE="logs/etl_$(date +%Y%m%d).log"

for script in "$SQL_DIR"/*.sql; do
    echo "Executing $script" >> "$LOG_FILE"
	echo "Executing $script" 
    sqlite3 "$DB_PATH" < "$script" >> "$LOG_FILE" 2>&1
done
