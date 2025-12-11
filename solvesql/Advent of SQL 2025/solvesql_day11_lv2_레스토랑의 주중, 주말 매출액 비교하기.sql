select
  case 
    when day in ('Sun', 'Sat') then 'weekend'
    else 'weekday'
  end as week,
  sum(total_bill) as sales
from tips
group by 
  case 
    when day in ('Sun', 'Sat') then 'weekend'
    else 'weekday'
  end
order by sales desc;