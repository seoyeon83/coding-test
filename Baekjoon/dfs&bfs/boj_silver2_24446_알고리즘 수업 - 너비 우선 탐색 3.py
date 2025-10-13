'''
노드 깊이 출력
시작 정점은 0, 방문되지 않은 경우는 -1 
깊이란... 

노드를 queue에 넣을 때 이전에 방문한, 선행 노드를 같이 기록하도록 해서 해결
'''
import sys
from collections import deque


def dfs(graph, start):
    queue = deque([(start, start)]) 
    visited = set()

    depth = {n:-1 for n in range(1, N+1)}

    while queue:
        n, p = queue.popleft()
        if n not in visited:
            visited.add(n)
            depth[n] = depth[p] + 1
            
            for i in graph[n]:
                if i not in visited:
                    queue.append((i, n))

    return depth

N, M, R = map(int, sys.stdin.readline().split())

graph = {n:[] for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for k, v in dfs(graph, R).items():
    print(v)