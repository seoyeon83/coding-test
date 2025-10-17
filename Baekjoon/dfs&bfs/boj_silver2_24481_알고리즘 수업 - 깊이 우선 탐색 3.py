import sys


def dfs(graph, start):
    visited = set()
    stack = [(start, start)]
    depth = {n:-1 for n in range(1, N+1)}

    while stack:
        n, p = stack.pop()
        if n not in visited:
            visited.add(n)
            depth[n] = depth[p] + 1
            for i in reversed(graph[n]):
                stack.append([i, n])

    return depth


N, M, R = map(int, sys.stdin.readline().split())

graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in range(1, N+1):
    graph[n].sort()

depth = dfs(graph, R)

for n in range(1, N+1):
    print(depth[n])