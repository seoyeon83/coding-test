SELECT
  ROUND(
    SUM(
      CASE
        WHEN LOWER(credit) LIKE '%gift%' THEN 1
        ELSE 0
      END
    ) / COUNT(*) * 100,
    3
  ) AS ratio
FROM
  artworks