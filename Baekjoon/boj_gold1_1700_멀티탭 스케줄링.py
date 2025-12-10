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