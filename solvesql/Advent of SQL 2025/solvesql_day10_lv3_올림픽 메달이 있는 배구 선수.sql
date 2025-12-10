/**
여자배구 대표팀이 메달을 딴 적이 있는가?
메달을 여러 개 가진 경우는 쉼표로 하나의 컬럼에 출력 << 이거 어떻게 하는 건데요
**/

with t as
(
  select r.athlete_id, medal
  from events e
  join records r on e.id = r.event_id
  join teams t on t.id = r.team_id
  where e.event = 'Volleyball Women''s Volleyball'
    and t.team = 'KOR'
    and r.medal IS NOT NULL
)
select a.id, 
    a.name, 
    group_concat(t.medal separator ',') as medals
from t
join athletes a on a.id = t.athlete_id
group by a.id, a.name;


/**
-> 근데 데이터에 여러 메달을 가진 경우가 없어서 위 경우에 대한 처리를 해주지 않아도 성공한다는 문제가 있음
하지만 공부를 위해 어떻게 하는 건지 한 번 찾아봐야겠다
group_concat!!

그리고 cte를 쓰지 않고 단일 쿼리를 쓰는 것으로 수정했다
**/


select 
    a.id, 
    a.name, 
    group_concat(t.medal separator ',') as medals
from athletes a
join records r on a.id = r.athlete_id
join events e on e.id = r.event_id
join teams t on t.id = r.team_id
where e.event = 'Volleyball Women''s Volleyball'
    and t.team = 'KOR'
    and r.medal IS NOT NULL
group by a.id, a.name;