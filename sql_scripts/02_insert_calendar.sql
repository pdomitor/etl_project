-- 2. Insertar fechas de enero 2025
WITH RECURSIVE dates(date_id) AS (
  SELECT DATE('2025-01-01')
  UNION ALL
  SELECT DATE(date_id, '+1 day')
  FROM dates
  WHERE date_id < DATE('2025-01-31')
)
INSERT INTO calendar(date_id)
SELECT date_id FROM dates;
