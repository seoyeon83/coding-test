'''
이것도 dfs/bfs 같은딩... bfs일듯........ 최단경로...? 잖아

나이트가 이동할 수 있는 칸의 경우의 수를 dx, dy로 정의
나이트가 이동할 수 있는 범위는 현 위치 좌표로부터 
-2, -1
-2, +1
+2, -1
+2, +1

-1, -2
-1, +2
+1, -2
+1, +2

쉽게 하는 건.. dx, dy
최소 몇 번만에 이동할 수 있는가?

bfs로 이동하는 경우마다 그 칸에 도달할 수 있는 최솟값을 탐색하게 됨
-1은 아직 도달하지 않는 경우
0은 start 지점

bfs.. 이전에 방문한 좌표를 알고 있어야만 한다
'''

import sys 
from collections import deque

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

def bfs(x, y, graph):
    queue = deque([((x, y), (x, y))])

    while queue:
        n, pn = queue.popleft()
        x,  y = n
        px, py = pn
        if 0 <= x < I and 0 <= y < I and graph[x][y] < 0:
            # 최단거리 갱신
            graph[x][y] = graph[px][py] + 1

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] < 0:
                    queue.append(((nx, ny), (x, y)))
    


for _ in range(int(sys.stdin.readline())):
    I = int(sys.stdin.readline())
    graph = [[-1]*I for _ in range(I)]

    sx, sy = map(int, sys.stdin.readline().split())
    # graph[sx][sy] = 0

    tx, ty = map(int, sys.stdin.readline().split())

    bfs(sx, sy, graph)

    print(graph[tx][ty])