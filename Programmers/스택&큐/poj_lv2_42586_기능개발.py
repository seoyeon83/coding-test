'''
작업 완료되는 것이 생길 때까지 반복?
아니면 각 작업마다 몇 번의 횟수가 지나야 끝날 수 있는지 계산하고 산출하기?
100-93 = 7, 7/1 = 7일
100-30 = 70, 70/30 = 3일
100-55 = 45, 45/5 = 9일

먼저 작업이 끝난 것 pop, 그 뒤에 오는 작업이 pop한 것보다 짧으면 따라서 pop 아니면 다음으로 넘김
'''
import math

def solution(progresses, speeds):
    answer = []
    
    # 작업 소요일 계산
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    while days:
        n = days.pop(0)
        cnt = 1
        while days and days[0] <= n: # 그 다음 작업이 처음 pop한 것보다 짧거나 같으면 따라서 pop
            days.pop(0)
            cnt += 1
        answer.append(cnt)
            
    return answer


'''
260122에 다시 풀이함
'''

from math import ceil

def solution(progresses, speeds):
    # 프로세스별 완성까지 걸리는 일 수 계산 
    days = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    # 결과 도출
    q = days[::-1]
    answer, idx, day = [0], 0, q[-1]
    while q:
        cur_day = q.pop()
        answer[idx] += 1
        
        # 더이상 그 날에 배포할 완료된 프로세스가 없음
        if q and q[-1] > day:
            idx += 1
            answer.append(0)
            day = q[-1]

    return answer

'''
260122
deque 활용
'''
from math import ceil
from collections import deque

def solution(progresses, speeds):
    # 프로세스별 완성까지 걸리는 일 수 계산 
    days = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    # 결과 도출
    queue = deque(days)
    answer, idx, day = [0], 0, queue[0]
    while queue:
        queue.popleft()
        answer[idx] += 1
        
        # 더이상 그 날에 배포할 완료된 프로세스가 없음
        if queue and queue[0] > day:
            idx += 1
            answer.append(0)
            day = queue[0]

    return answer


'''
260122
첫 번째로 풀었던 방식과 합친 것
=> 가장 이상적인 방식인듯!
'''
from math import ceil
from collections import deque

def solution(progresses, speeds):
    # 프로세스별 완성까지 걸리는 일 수 계산 
    days = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    # 결과 도출
    queue = deque(days)
    answer = list()
    while queue:
        n = queue.popleft()
        cnt = 1
        
        while queue and n >= queue[0]:
            queue.popleft()
            cnt += 1
        
        answer.append(cnt)
        
    return answer

'''
260616
이전에 풀었던 것보다 더 퇴화했다.. 하하
deque를 쓰는 이유가 popleft() O(1)을 위해서인데, 그 안에서 인덱스 접근을 하는 것이 충돌... 
하긴 생각해보니 큐인데 인덱스로 계산을 한다는 것이 맞지 않는 게 이해가 된다
개선: 미리 완료까지 걸리는 일수를 계산할 것
    => days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
'''

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        answer.append(cnt)
        
    return answer

# 개선
import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    max_day = days[0]
    cnt = 1

    for d in days[1:]:
        if d <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_day = d 
        
    answer.append(cnt)
    return answer

'''
260618 - 복습
기억을 기반으로 날짜 수 계산하고 answer을 계산하는 방법으로 진행
날짜 계산 로직은 괜찮았는데, answer 로직 계산 코드가 좀 헷갈려서 시간이 걸렸지만 결국 혼자 풀었다!
개선:
    1) 날짜 계산 시, range 말고 zip 사용
'''
import math

def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    answer = [1]
    cur_day = days[0]
    for day in days[1:]:
        if day <= cur_day:
            answer[-1] += 1
        else:
            answer.append(1)
            cur_day = day
            
    return answer
# 개선
import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = [1]
    cur_day = days[0]
    for day in days[1:]:
        if day <= cur_day:
            answer[-1] += 1
        else:
            answer.append(1)
            cur_day = day
            
    return answer