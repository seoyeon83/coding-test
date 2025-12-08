select
  *
from
  wines
where
  color = 'white'
  and quality >= 7
  and residual_sugar > (select avg(residual_sugar) from wines)
  and density > (select avg(density) from wines)
  and pH < (select avg(pH) from wines where color = 'white')
  and citric_acid > (select avg(citric_acid) from wines where color = 'white');