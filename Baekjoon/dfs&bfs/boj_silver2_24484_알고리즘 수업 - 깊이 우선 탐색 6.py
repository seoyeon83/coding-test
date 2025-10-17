'''
dep, seq 둘 다 구해서 곱하기
내림차순
'''

import sys 


def dfs(graph, start):
    visited = set()

    stack = [(start, start)]

    dep = {n:-1 for n in range(1, N+1)}
    seq = {n:0 for n in range(1, N+1)}
    s = 1

    while stack:
        n, p = stack.pop()
        if n not in visited:
            visited.add(n)
            dep[n] = dep[p] + 1
            seq[n] = s
            s += 1
            for i in reversed(graph[n]):
                if i not in visited:
                    stack.append((i, n))
    
    return dep, seq


N, M, R = map(int, sys.stdin.readline().split())

graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in range(1, N+1):
    graph[n].sort(reverse=True)


dep, seq = dfs(graph, R)
ans = 0
for n in range(1, N+1):
    ans += (dep[n] * seq[n])
print(ans)