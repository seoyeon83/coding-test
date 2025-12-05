'''
N개의 회의에 대한 회의실 사용표를 만들 예정
각 회의 I에 대해 시작 시간과 끝나는 시간이 주어짐
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자 

회의가 끝나는 동시에 다음 회의가 시작될 수 있다
회의별로 시작 시간과 종료 시간이 같을 수 있다. 시작하자마자 끝나는 것..

최대 사용할 수 있는 회의의 최대 개수. 즉, 가장 많은 회의가 진행되어야 하는 것
소요 시간과 시작 시간으로 정렬을 해야할까? 일단 소요 시간이 짧은 걸 기준으로 넣고
그 시간에 회의실이 비어있으면(마지막 회의 종료 시간이 현재 회의 시작 시간보다 같거나 이전이면) 회의 진행
0 ~ 2^31-1

끝나는 시간, 시작하는 시간 기준으로 정렬하면 될듯!!! 
'''

import sys

N = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0], x[1]-x[0]))

inprogess_meeting = meetings[0]
answer = 1
for meeting in meetings[1:]:
    if inprogess_meeting[1] <= meeting[0]:
        inprogess_meeting = meeting
        answer += 1

print(answer)