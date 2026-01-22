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