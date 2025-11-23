'''
리스트 배열? 로 저장해서 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그 영역의 넓이가 얼마인지
bfs? dfs? 중 하나로 풀기

탐색하면서 영역의 넓이 수집

'''

import sys 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, graph):
    cnt = 0
    stack = list([(x, y)])
    
    while stack:
        x, y = stack.pop()
        if graph[x][y] == 0:
            graph[x][y] = 1
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                    stack.append((nx, ny))
    
    return cnt

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    # 왼쪽 아래 꼭짓점의 x, y와 오른쪽 위 꼭짓점의 x, y
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = -1


answer = list()
for x in range(M):
    for y in range(N):
        if graph[x][y] == 0:
            answer.append(dfs(x, y, graph))

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=" ")