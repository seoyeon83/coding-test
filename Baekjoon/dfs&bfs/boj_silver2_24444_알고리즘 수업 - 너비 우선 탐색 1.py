from collections import deque
import sys

def bfs(graph, R):
    queue = deque([R])
    visited = set()

    # 방문 순서 기록 
    cnt = {n:0 for n in range(1, N+1)}
    c = 1

    while queue:
        n = queue.popleft()
        if n not in visited:
            # 방문 처리
            visited.add(n)
            cnt[n] = c
            c += 1
            for i in graph[n]:
                if i not in visited:
                    queue.append(i)
    
    return cnt

N, M, R = map(int, sys.stdin.readline().split())

graph = {n:[] for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 연결된 노드를 오름차순으로 정렬
for i in range(1, N+1):
    graph[i].sort()

# 결과 출력
for k, v in bfs(graph, R).items():
    print(v)