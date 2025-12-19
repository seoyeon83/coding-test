SELECT 
  YEAR(purchased_at) AS year,
  SUM(CASE
    WHEN shipping_method != 'Standard' AND is_returned IS TRUE THEN 1
    WHEN shipping_method = 'Standard' AND is_returned IS FALSE THEN 1
    WHEN shipping_method = 'Standard' AND is_returned IS TRUE THEN 2
    ELSE 0
  END) AS standard,
  SUM(CASE
    WHEN shipping_method = 'Express' THEN 1
    ELSE 0
  END) AS express,
  SUM(CASE
    WHEN shipping_method = 'Overnight' THEN 1
    ELSE 0
  END) AS overnight
FROM transactions
GROUP BY YEAR(purchased_at)
ORDER BY year ASC;