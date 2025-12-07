SELECT
  rd.measured_at as date_alert
from
  measurements st,
  measurements nd,
  measurements rd
where
  datediff(nd.measured_at, st.measured_at) = 1 
  and st.pm10 < nd.pm10
  and datediff(rd.measured_at, nd.measured_at) = 1
  and nd.pm10 < rd.pm10
  and rd.pm10 >= 30
order by
  date_alert;