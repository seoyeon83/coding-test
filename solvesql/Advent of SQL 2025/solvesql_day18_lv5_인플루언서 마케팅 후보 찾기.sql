WITH all_edges AS (
  SELECT user_a_id AS u1, user_b_id AS u2 FROM edges
  UNION ALL 
  SELECT user_b_id AS u1, user_a_id AS u2 FROM edges
),
friend_counts AS (
  SELECT u1 AS user_id, COUNT(*) AS friends
  FROM all_edges
  GROUP BY u1
)
SELECT 
  e.u1 AS user_id,
  COUNT(*) AS friends,
  SUM(f.friends) AS friends_of_friends,
  ROUND(SUM(f.friends) / COUNT(*), 2) AS ratio
FROM all_edges e 
JOIN friend_counts f ON e.u2 = f.user_id
GROUP BY e.u1
HAVING COUNT(*) >= 100
ORDER BY ratio DESC
LIMIT 5;