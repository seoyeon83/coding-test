'''
연결 요소의 개수..?
무방향 그래프 
연결 요소란? 서로 연결되어 모여있는 집합들 개수

그래프 속 1부터 n까지의 노드를 순회하면서 각각 dfs나 bfs 수행하면 되겠다
'''

import sys


N, M = map(int, sys.stdin.readline().split())
graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
answer = 0
for n in range(1, N+1):
    if n not in visited:
        stack = [n]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.add(n)
                for i in reversed(graph[n]):
                    if i not in visited:
                        stack.append(i)
    
        answer += 1

print(answer)