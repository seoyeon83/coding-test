'''
연구소
바이러스는 상하좌우 인접한 빈 칸으로 퍼질 수 있다
벽 3개 세우기

벽 3개를 세운 뒤 바이러슥 퍼질 수 없는 곳인 안전 영역 크기의 최댓값을 구하는 것

어디에 벽을 둬야 바이러스가 덜 퍼질 것인가?

완전탐색 + bfs

벽 세우기 조합 => 3개의 좌표 선택

0 ~ N-1 행
0 ~ M-1 인덱스

0: 빈 칸, 1: 벽, 2: 바이러스
'''

import sys
from itertools import combinations
from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바이러스 모두 퍼트리기
def bfs(graph, virus):
    queue = deque(virus)
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 2

    # 0 세기
    res = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                res += 1

    return res


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 빈 칸(0), 바이러스(2) 좌표 찾기
empty = list()
virus = list()
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            empty.append((x, y))
        if graph[x][y] == 2:
            virus.append((x, y))

ans = 0
for a in combinations(empty, 3):
    copy_graph = list()
    for g in graph:
        copy_graph.append(g.copy())
        
    for r, c in a:
        copy_graph[r][c] = 1

    res = bfs(copy_graph, virus)
    ans = max(res, ans)

print(ans)