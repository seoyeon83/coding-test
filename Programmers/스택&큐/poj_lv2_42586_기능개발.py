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