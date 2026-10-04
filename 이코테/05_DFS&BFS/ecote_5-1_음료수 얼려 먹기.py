'''
261004

N * M 얼음 틀
구멍 0, 칸막이 1
구멍 뚫린 부분끼리 상하좌우로 붙어있으면 서로 연결된 것
생성되는 총 아이스크림의 개수

0, 0 ~ N, M까지 탐색하면서 방문하거나 벽인 경우는 넘어가고, 0인 경우 dfs?나 bfs 수행
이거는 visited 를 표기하긴 하는데 뭐 방문한 노드나 이런 게 중요한 게 아니라
탐색 수행 횟수를 세야하는 것임. 이번엔 bfs 반복문으로 한 번 해봐야겠다~

4 5
00110
00011
11111
00000

근데 헷갈리는 게... 함수 안에서 graph 바꾸면 나와서도 똑같나 => 똑같네
'''

import sys
from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '0':
                graph[nx][ny] = '-1'
                queue.append((nx, ny))
    

N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == '0':
            bfs(graph, x, y)
            answer += 1

print(answer)


# 재귀 dfs로 푸는 방식 (교재 정답)

import sys

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == '0':
        graph[x][y] = '1'
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
            answer += 1

print(answer)
