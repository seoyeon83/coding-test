WITH 
  t1 AS (
    SELECT 
      customer_id, 
      city_id, 
      SUM(total_price - discount_amount) AS total_spent 
    FROM transactions 
    WHERE is_returned IS FALSE
    GROUP BY customer_id, city_id
  ),
  t2 AS (
    SELECT 
      customer_id, 
      city_id, 
      total_spent,
      ROW_NUMBER() OVER (PARTITION BY city_id ORDER BY total_spent DESC) AS ranking
    FROM t1
  )

SELECT
  city_id,
  customer_id,
  total_spent
FROM t2
WHERE ranking = 1;