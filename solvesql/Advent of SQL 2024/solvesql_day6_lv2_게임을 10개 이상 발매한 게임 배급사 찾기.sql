SELECT c.name
FROM games g
JOIN companies c ON g.publisher_id = c.company_id
GROUP BY company_id
HAVING COUNT(*) >= 10; 