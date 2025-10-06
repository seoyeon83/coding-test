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