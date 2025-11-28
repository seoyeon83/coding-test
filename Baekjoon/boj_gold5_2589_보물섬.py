'''
육지 L or 바다 W
상하좌우로 이웃한 육지로만 이동이 가능함
보물은 서로 간에 최단거리로 이동하는 데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀 있다
같은 곳을 두 번 이상 지나가거나 멀리 돌아가면 안됨

그러면 각 위치별로 가장 먼 곳까지의 최단거리를 구하고...
각각 위치 중에서도 최대값을 구해서 출력해야하네

최단거리는 뭐다? bfs!

그래프 내 최대값은 마지막으로 저장했던 위치 
땅은 0, 바다는 -1 로
'''

import sys 
from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    graph2 = copy.deepcopy(graph)
    queue = deque([[[x, y], [x, y]]])

    while queue:
        n, np = queue.popleft()
        x, y = n
        px, py = np
        if graph2[x][y] == 0:
            graph2[x][y] = graph2[px][py] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and graph2[nx][ny] == 0:
                    queue.append([[nx, ny], [x, y]])
                
    return graph2[x][y] - 1



N, M = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        graph[i][j] = -1 if graph[i][j] == 'W' else 0

answer = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            result = bfs(graph, x, y)
            if result > answer:
                answer = result

print(answer)