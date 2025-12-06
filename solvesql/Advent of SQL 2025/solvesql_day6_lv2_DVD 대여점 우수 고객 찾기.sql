select
  customer_id
from
  rental r
  join customer c using (customer_id)
where
  c.active = TRUE
group by
  customer_id
having
  count(*) >= 35;