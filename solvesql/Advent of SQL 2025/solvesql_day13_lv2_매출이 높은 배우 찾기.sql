select a.first_name, a.last_name, sum(p.amount) as total_revenue
from rental r
join payment p on r.rental_id = p.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film_actor f on f.film_id = i.film_id
join actor a on a.actor_id = f.actor_id
group by a.actor_id, a.first_name, a.last_name
order by total_revenue desc
limit 5;