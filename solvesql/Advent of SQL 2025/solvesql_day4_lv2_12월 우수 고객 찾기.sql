select
  customer_id
from
  records
where
  left(order_date, 7) = '2020-12'
group by
  customer_id
having
  sum(sales) >= 1000;