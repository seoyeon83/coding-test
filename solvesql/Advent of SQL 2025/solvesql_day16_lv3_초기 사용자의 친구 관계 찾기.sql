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


-- 251227 재시도!
-- COUNT(*) OVER() 은 생각해내지 못했지만 그래도 성공했다
WITH elements AS (
  SELECT
    user_a_id,
    user_b_id,
    user_a_id + user_b_id AS id_sum,
    RANK() OVER(ORDER BY user_a_id + user_b_id ASC) AS ranking,
    (SELECT COUNT(*) AS cnt FROM edges) AS cnt
  FROM edges
)

SELECT user_a_id, user_b_id, id_sum
FROM elements
WHERE ranking / cnt <= 0.001;