-- 25달러 이상 2개, 15달러 이상, 1개
-- 15달러 미만, 15달러 이상 25달러 미만, 25달러 이상 으로 나누어서 집계하는 것이 필요함

select
  case
    when total_bill < 15 then 0
    when total_bill < 25 then 1
    else 2
  end as stamp,
  count(*) as count_bill
from
  tips
group by
  case
    when total_bill < 15 then 0
    when total_bill < 25 then 1
    else 2
  end
order by
  stamp asc;

-- 251225 다시 풀어보았음! 한 번에 성공 ㅎㅎ
SELECT 
  CASE
    WHEN total_bill >= 25 THEN 2
    WHEN total_bill >= 15 THEN 1
    ELSE 0
  END AS stamp,
  COUNT(*) AS count_bill
FROM tips
GROUP BY stamp
ORDER BY stamp ASC;