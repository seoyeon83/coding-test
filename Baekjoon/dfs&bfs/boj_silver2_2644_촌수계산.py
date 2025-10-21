'''
부모 - 자식은 1촌
조모 - 자식은 2촌
즉, 루트부터 계층을 구하고 두 인물의 레벨 차이를 구하는 것
방향그래프..................? 

bfs로 탐색하면서 루트부터 레벨을 구한다?
아니면 양방향 그래프로 표현하고, bfs로 거리를 구할까?
찾지 못한 경우에는 -1 반환
'''

import sys 
from collections import deque


def bfs(graph, start, target):
    visited = set()
    queue = deque([[start, start]])
    
    distance = {n:-1 for n in range(1,N+1)}
    
    while queue:
        n, p = queue.popleft()
        if n not in visited:
            visited.add(n)
            distance[n] = distance[p] + 1
            for i in graph[n]:
                if i not in visited:
                    queue.append([i, n])

    
    return distance[target]


N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())
graph = {n:list() for n in range(1,N+1)}
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

print(bfs(graph, a, b))
