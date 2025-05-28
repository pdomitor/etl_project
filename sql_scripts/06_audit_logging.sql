 CREATE TABLE IF NOT EXISTS etl_log (
    run_time TEXT,
    rows_inserted INTEGER
);

INSERT INTO etl_log (run_time, rows_inserted)
VALUES (datetime('now'), (SELECT COUNT(*) FROM daily_revenue_jan2025));