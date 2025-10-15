import sys


def dfs(graph, start):
    visited = set()
    stack = [start]
    seq = {n:0 for n in range(1, N+1)}
    cnt = 1

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            seq[n] = cnt
            cnt += 1
            for i in reversed(graph[n]):
                if i not in visited:
                    stack.append(i)
    
    return seq


N, M, R = map(int, sys.stdin.readline().split())

graph = {n:list() for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in range(1, N+1):
    graph[n].sort()

seq = dfs(graph, R)

for n in range(1, N+1):
    print(seq[n])

### 재귀로 풀어보려 한 흔적... 하지만 재귀횟수초과가 문제인지 런타임에러가 뜨더라
# import sys
# def dfs(graph, n, visited, seq):
#     visited.add(n)
#     cnt += 1
#     seq[n] = cnt
    
#     for i in graph[n]:
#         if i not in visited:
#             dfs(graph, i, visited, seq)


# N, M, R = map(int, sys.stdin.readline().split())

# graph = {n:list() for n in range(1, N+1)}
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for n in range(1, N+1):
#     graph[n].sort()


# seq = {n:0 for n in range(1, N+1)}
# visited = set()
# cnt = 0

# dfs(graph, R, visited, seq)

# for n in range(1, N+1):
#     print(seq[n])