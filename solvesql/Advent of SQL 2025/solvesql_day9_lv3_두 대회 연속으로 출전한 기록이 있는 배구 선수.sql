/**
올림픽에 연달아 참여한 여자 배구 선수
배구는 하계에만 하므로 하계 올림픽만 조회해야 함 (Summer)

여자 배구 종목 여부는 events.event = 'Volleyball Women''s Volleyball'
 -> 경기 id -> records.event_id 도출
대한민국 국가대표팀 여부는 teams.team = 'KOR' -> 팀 ID -> records.team_id
하계 올림픽 여부 -> games.season -> games.id -> records.game_id
일단 
서브쿼리에서 테이블 네개를 조인하는 건 좀 힘들 것 같아서 
cte와 서브쿼리를 이용해서 우선 조건에 맞는 선수 id와 올림픽 개최 연도를 가져옴
위까지를 cte를 이용해 t로 정의하고, athletes와 t를 조인, 
그리고 개최 연속된 개최를 찾기 위해 다시 t와 조인

gemini 피드백:
1) 4년 차이 취약성: 올림픽이 항상 4년 주기로 열리는 것은 아님. 하지만 데이터셋이 잘 정규화되어 있으면 괜찮음. 하지만 혹시모르니 다른 비교가 더욱 안전
2) 서브쿼리 IN으로 하는 것보다 일반적으로 join을 사용하는 것이 좋을 수 있다
3) 셀프 조인은 O(N^2)에 가까운 비용이 발생할 수 있으므로, LEAD()나 LAG()같은 윈도우 함수를 사용해보자
**/

-- 처음 성공한 쿼리
with t as (
  select r.athlete_id, g.year
  from records r join games g on(r.game_id = g.id)
  where r.event_id IN (select id from events where event = 'Volleyball Women''s Volleyball')
    and r.team_id IN (select id from teams where team = 'KOR')
    and g.season = 'Summer'
  )
select distinct a.id, a.name
from athletes a
join t t1 on(a.id = t1.athlete_id)
join t t2 on(t1.athlete_id = t2.athlete_id and t2.year - t1.year = 4);


-- 개선한 버전
-- 윈도우 함수로 다음 참가 연도 가져오기
-- 서브쿼리 대신 join

with t as (
  select 
    r.athlete_id, 
    g.year,
    -- 선수별로 연도순 정렬 후 바로 다음 참가 연도를 가져온다
    LEAD(g.year) OVER (PARTITION BY r.athlete_id ORDER BY g.year) as next_year
  from records r 
  join games g on r.game_id = g.id
  join events e on r.event_id = e.id
  join teams t on r.team_id = e.id
  where e.event = 'Volleyball Women''s Volleyball'
    and t.team = 'KOR'
    and g.season = 'Summer'
  )
select distinct a.id, a.name
from athletes a
join t t1 on a.id = t1.athlete_id
where t.next_year - t.year = 4);