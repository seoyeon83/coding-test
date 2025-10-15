'''
너비 우선 탐색으로 만들어지는 트리 -> 너비 우선 탐색 트리 
i번 노드의 깊이는 di. R의 깊이는 0. 방문되지 않는 노드의 깊이는 -1.
모든 노드에 대한 노드 방문 순서 t * 노드 트리 깊이 d 의 합을 구한다 
'''
import sys
from collections import deque


def bfs(graph, start):
    queue = deque([(start, start)])
    visited = set()

    depth = {n:-1 for n in range(1, N+1)}
    seq = {n:0 for n in range(1, N+1)}
    s = 1
    while queue:
        n, p = queue.popleft()
        if n not in visited:
            visited.add(n)
            depth[n] = depth[p] + 1
            seq[n] = s
            s += 1
            for i in graph[n]:
                if i not in visited:
                    queue.append((i, n))
                    

    return depth, seq

N, M, R = map(int, sys.stdin.readline().split())

graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for n in range(1, N+1):
    graph[n].sort()

depth, seq = bfs(graph, R)

ans = 0
for n in range(1, N+1):
    ans += depth[n] * seq[n]

print(ans)