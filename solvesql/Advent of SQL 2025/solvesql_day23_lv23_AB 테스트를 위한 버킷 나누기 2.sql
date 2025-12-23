WITH customer AS (
  SELECT 
    customer_id, 
    SUM(
      CASE
        WHEN is_returned IS FALSE THEN 1
        ELSE 0
      END 
    ) AS orders,
    SUM(
      CASE
        WHEN is_returned IS FALSE THEN total_price
        ELSE 0
      END 
    ) AS revenue
  FROM transactions
  GROUP BY customer_id
)


SELECT 
  CASE
    WHEN customer_id % 10 = 0 THEN 'A'
    ELSE 'B'
  END AS bucket,
  COUNT(customer_id) AS user_count,
  ROUND(AVG(orders), 2) AS avg_orders,
  ROUND(AVG(revenue), 2) AS avg_revenue
FROM customer
GROUP BY bucket;