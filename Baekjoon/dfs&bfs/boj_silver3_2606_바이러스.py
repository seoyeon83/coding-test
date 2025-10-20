'''
한 컴퓨터가 바이러스에 걸리면 연결된 모든 컴퓨터도 걸리게 됨 
1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력

bfs든 dfs든 상관없네 그럼
'''
from collections import deque
import sys 

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.add(n)
            for i in graph[n]:
                if i not in visited:
                    queue.append(i)

    return len(visited)



N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, 1)-1)