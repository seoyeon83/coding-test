WITH
  ranking AS (
    SELECT
      user_a_id,
      user_b_id,
      user_a_id + user_b_id AS id_sum,
      ROW_NUMBER() OVER (ORDER BY user_a_id + user_b_id ASC) AS element_rank,
      COUNT(*) OVER () AS total_count
    FROM
      edges
  )
SELECT
  user_a_id,
  user_b_id,
  id_sum
FROM
  ranking
WHERE
  CAST(element_rank AS DECIMAL) / total_count <= 0.001;