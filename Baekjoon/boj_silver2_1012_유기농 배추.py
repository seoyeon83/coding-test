'''
배추흰지렁이
배추에 한 마리라도 살고 있으면 인접한 다른 배추로 이동할 수 있고, 역시 보호받을 수 있다
배추들이 모여있는 곳에는 한 마리만 있으면 된다

이거 그냥 dfs, bfs로 군집 개수를 세면 되겠다
'''

import sys


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if graph[x][y] > 0:
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] > 0:
                    stack.append((nx, ny))


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    answer = 0
    for x in range(M):
        for y in range(N):
            if graph[x][y] > 0:
                dfs(graph, x, y)
                answer += 1
    
    print(answer)