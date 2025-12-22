/**
전체적으로 잘 생각해냈는데, WEEKDAY(), IFNULL() 등 함수명을 잘 몰랐던 것, 
그리고 LAG() 함수 사용법을 제대로 기억 못했던 것 때문에...
나중에 다시 풀어보자
**/

WITH elements AS (
  SELECT 
    DATE(purchased_at) AS order_date, 
    CASE WEEKDAY(purchased_at)
      WHEN '0' THEN 'Monday'
      WHEN '1' THEN 'Tuesday'
      WHEN '2' THEN 'Wednesday'
      WHEN '3' THEN 'Thursday'
      WHEN '4' THEN 'Friday'
      WHEN '5' THEN 'Saturday'
      WHEN '6' THEN 'Sunday'
    END AS weekday,
    COUNT(*) AS num_orders_today
  FROM transactions
  WHERE is_online_order IS TRUE AND YEAR(purchased_at) = 2023
  GROUP BY order_date, weekday
)

SELECT 
  order_date,
  weekday,
  num_orders_today,
  num_orders_today + IFNULL(LAG(num_orders_today) OVER(ORDER BY order_date), 0) AS num_orders_from_yesterday
FROM elements
ORDER BY order_date;