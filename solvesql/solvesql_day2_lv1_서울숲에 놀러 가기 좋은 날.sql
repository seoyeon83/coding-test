select
  measured_at as 'good_day'
from
  measurements
where
  left(measured_at, 7) = '2022-12'
  and pm2_5 <= 9
order by
  measured_at asc;