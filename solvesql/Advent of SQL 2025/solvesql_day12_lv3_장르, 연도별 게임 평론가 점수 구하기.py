/**
2011 ~   2015 각 장르의  평론가 점수 평균 계산
연도별 평론가 점수 평균, 점수 없는 건 제외, 소수점 둘째자리까지 계산

피벗 테이블.. 기억이 안 난다 어떻게 하는 거였는지
-> 어떻게 하는지 찾아보고 진행.. 다음에 다시 풀어봅시다
**/
SELECT
  ge.name AS genre,
  ROUND(
    AVG(
      CASE
        WHEN ga.year = 2011 THEN ga.critic_score
        ELSE NULL
      END
    ),
    2
  ) AS score_2011,
  ROUND(
    AVG(
      CASE
        WHEN ga.year = 2012 THEN ga.critic_score
        ELSE NULL
      END
    ),
    2
  ) AS score_2012,
  ROUND(
    AVG(
      CASE
        WHEN ga.year = 2013 THEN ga.critic_score
        ELSE NULL
      END
    ),
    2
  ) AS score_2013,
  ROUND(
    AVG(
      CASE
        WHEN ga.year = 2014 THEN ga.critic_score
        ELSE NULL
      END
    ),
    2
  ) AS score_2014,
  ROUND(
    AVG(
      CASE
        WHEN ga.year = 2015 THEN ga.critic_score
        ELSE NULL
      END
    ),
    2
  ) AS score_2015
FROM
  genres ge
  JOIN games ga ON ge.genre_id = ga.genre_id
GROUP BY
  ge.name