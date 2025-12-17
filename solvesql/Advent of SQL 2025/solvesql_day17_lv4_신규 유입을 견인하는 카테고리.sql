WITH distinct_records AS (
  SELECT DISTINCT order_date, customer_id, order_id, category, sub_category
  FROM records
)

SELECT 
  category, 
  sub_category, 
  COUNT(*) AS cnt_orders
FROM customer_stats c 
JOIN distinct_records r ON c.customer_id = r.customer_id AND c.first_order_date = r.order_date
GROUP BY category, sub_category
ORDER BY cnt_orders DESC;