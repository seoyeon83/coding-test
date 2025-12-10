'''
한 개의 멀티탭, 
플러그를 빼는 횟수를 최소화

일단 사용 횟수가 많을 수록 안 빼는 게 이득
사용 횟수가 많은 건 고정적으로 끼워두고 비교적 덜 왔다갔다하는 걸 해야하는데..
그 기준을 어떻게 할 거냐는 것 
많이 쓰지만 길게 쓰지 않는 것도.. 어떻게?

일단 순서대로 꽂는데, 다음에 사용 계획이 있는 경우는 빼지 않는다
그리고 모두 사용 계획이 있는 경우, 가장 나중에 사용할 것을 뺀다
'''

import sys 


# 멀티탭 구멍 개수, 총 사용 횟수
N, K = map(int, sys.stdin.readline().split())
apps =  list(map(int, sys.stdin.readline().split()))

powers = list()
answer = 0
# 순서대로 하는데, 만약 이미 꽂혀있으면 넘어가기
# 꽂혀있지 않다면 빼야할 것을 선택해야 함
# 기준은?
# 1. 나중에 또 쓸 계획이 있는가?
# 2. 모두 쓸 계획이 잇다면, 근시일 내에 쓸 계획이 있는가?
# 이걸 어떻게 판별하면 좋을까 
for i in range(len(apps)):
    if apps[i] in powers: continue
    if len(powers) < N: 
        powers.append(apps[i])
        continue

    # 1. 나중에 또 쓸 계획이 있는가?
    c = list()
    for j, a in enumerate(powers):
        if a not in apps[i:]:
            c.append(j)

    if c:
        powers[c[0]] = apps[i]
    # 2. 모두 쓸 계획이 있다면, 근시일 내에 쓸 계획이 있는가?
    else:
        for j, a in enumerate(powers):
            c.append((j, apps[i:].index(a)))
        c.sort(key=lambda x: x[1], reverse=True) # 가장 근시일에 사용할 예정이 없는 것
        powers[c[0][0]] = apps[i]

    answer += 1


print(answer)



'''
### 정답은 통과했는데.. 이게 좋은 코드일까? (Gemini에게 물어보자)

와.. 코드 잘 짠다...
이렇게 짤 수도 있구나 너무 신기하다!!!
try-except를 활용하는 게 인상적이다 앞으로는 if-else보다도 이렇게 코드를 짜보도록 해봐야겠다
'''
import sys

# 입력 처리
N, K = map(int, sys.stdin.readline().split())
apps = list(map(int, sys.stdin.readline().split()))

plugged = [] # 멀티탭에 꽂힌 기기들 (powers 대신 더 직관적인 이름 사용)
answer = 0

for i, app in enumerate(apps):
    # 1. 이미 꽂혀있는 경우
    if app in plugged:
        continue
    
    # 2. 빈 자리가 있는 경우
    if len(plugged) < N:
        plugged.append(app)
        continue
    
    # 3. 꽉 차서 하나를 빼야 하는 경우 (가장 핵심 로직)
    target_idx = -1     # 뺄 기기의 인덱스 (plugged 리스트 내의 위치)
    latest_usage = -1   # 가장 늦게 사용되는 시점

    for idx, p in enumerate(plugged):
        try:
            # 현재 시점(i) 이후에 해당 기기(p)가 언제 나오는지 확인
            # apps[i+1:] 에서 p의 위치를 찾음
            next_use = apps[i+1:].index(p)
        except ValueError:
            # 앞으로 사용할 일이 없다면 최우선 제거 대상
            target_idx = idx
            break 
        
        # 가장 늦게 사용되는 기기를 갱신
        if next_use > latest_usage:
            latest_usage = next_use
            target_idx = idx
            
    # 정해진 기기를 빼고 새 기기를 꽂음
    # (plugged 리스트의 값을 덮어쓰거나, pop 후 append)
    plugged[target_idx] = app 
    answer += 1

print(answer)