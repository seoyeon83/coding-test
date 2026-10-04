'''
261004

N * M 크기의 미로
동빈이 위치 (1, 1) 출구는 (N, M) 1-index
괴물 위치는 0, 없는 부분은 1
탈출하기 위해 움직여야 하는 최소 칸의 개수 (시작 칸, 마지막 칸 포함)

최단거리 문제네
최단거리 문제는 bfs로 해서 1,1 로부터 거리를 .. 그 칸에 기록하는 방식 아닌가?
그러면 queue에다가 방문 처리를 하면서 이전 칸의 값을 더해주는 형태로 방문 처리를 해야하는 거지

5 6
101010
111111
000001
111111
111111
=> 10

4 4
1111
1111
1111
1111
=> 7
'''

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph):
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x == (N-1) and y == (M-1):
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

print(bfs(graph))

