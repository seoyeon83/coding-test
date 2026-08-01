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

'''
# 260801
접근: 매번 전수조사해서 현재 프로세스보다 우선순위가 큰 경우를 확인한다
개선점:
    (1) 큐 안에 우선순위가 큰 경우를 탐색하는 건 any() 함수로 확인할 수 있다
    for문으로 여러 줄에 걸쳐 구현한 내용을 한 줄로 표현 가능하다 (와..)
    (2) 튜플 언패킹으로 인덱싱 ([0]) 없애기
    확실히 그러면 더 직관적인 코드가 되겠다

흐름 자체는 예전 풀이가 낫다는 피드백...
'''

from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    while queue:
        current_process = queue.popleft()
        
        # 현재 프로세스보다 우선순위가 큰 경우 탐색
        a = current_process[1]
        for _ in range(len(queue)):
            node = queue.popleft()
            a = node[1] if node[1] > a else a
            queue.append(node)
            
        # 우선순위가 큰 경우가 존재하면 다시 큐에 넣기, 아니면 프로세스 실행(answer + 1)
        if a > current_process[1]:
            queue.append(current_process)
        else:
            answer += 1
            if current_process[0] == location:
                return answer

# 개선


from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    while queue:
        idx, priority = queue.popleft()
            
        # 우선순위가 큰 경우가 존재하면 다시 큐에 넣기, 아니면 프로세스 실행(answer + 1)
        if any(node[1] > priority for node in queue):
            queue.append(priority)
        else:
            answer += 1
            if idx == location:
                return answer