from collections import deque

def solution(priorities, location):
    queue = deque()
    sorted_priorities = sorted(priorities)

    for p in enumerate(priorities):
        queue.append(p)
        
    for i in range(1, len(priorities)+1):
        q = queue.popleft()
        while queue and max(sorted_priorities)>q[1]:
            queue.append(q)
            q = queue.popleft()

        sorted_priorities.pop()
        if q[0] == location:
            return i
        

print(solution([2,1,3,2], 2))


'''
260126
'''

from collections import deque


def solution(priorities, location):
    # queue에 인덱스, 우선순위 tuple 형태로 저장 
    queue = deque()
    for p in enumerate(priorities):
        queue.append(p)
    
    # 우선순위 정렬 (높은 게 뒤로 오게, 오름차순으로)
    priorities.sort()

    # 순회하면서 프로세스 처리 (직접 세는 대신 for문을 쓰면 더 깔끔할 듯)
    cnt = 1
    while queue:
        mi, mp = queue.popleft()

        # 더 우선순위가 높은 프로세스가 있는지 탐색
        while priorities[-1] > mp:
            queue.append((mi, mp))
            mi, mp = queue.popleft()
    
        # 궁금한 프로세스가 처리된 경우 정답 return
        if mi == location:
            return cnt
        
        # 순번 업데이트
        cnt += 1
        # 처리된 프로세스의 우선순위 제거
        priorities.pop()