# bfs로 노드 방문 순서 출력 (내림차순)

import sys
from collections import deque

def dfs(graph, start):
    queue = deque([start])
    visited = set()

    cnt = {n:0 for n in range(1, len(graph)+1)}
    c = 1

    while queue:
        n = queue.popleft()
        if n not in visited:
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

for n in range(1, N+1):
    graph[n].sort(reverse=True)

for k, v in dfs(graph, R).items():
    print(v)