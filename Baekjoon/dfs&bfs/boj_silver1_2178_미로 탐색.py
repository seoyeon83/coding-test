'''
1은 이동할 수 있는 칸, 0은 아닌 칸
1,1에서 출발해 N,M의 위치로 이동할 때 지나야 하는 최소의 칸 수 
최단경로 구하는 문제 -> bfs (너비우선탐색)

queue로 구현
이전에 방문한 노드에서 지금 노드에 그 값을 더하는 방식
상하좌우를 모두 탐색
마지막에는 N, M 위치에 있는 값을 출력하면 됨 
'''


import sys
from collections import deque

def bfs(graph):
    visited = set()
    # 현재 노드(좌표) 및 이전에 방문했던 좌표 기록
    queue = deque([[(0, 0), (0, 0)]])

    while queue:
        n, p = queue.popleft()
        x, y = n
        px, py = p
        if graph[x][y] > 0 and n not in visited : # 지나갈 수 있는지, 방문한 적 있는지 검사 
            # 방문 처리 및 최단거리 기록 
            visited.add(n)
            graph[x][y] += graph[px][py]
            # 상하좌우 확인 및 queue에 append
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visited and nx >= 0 and nx < N and ny >= 0 and ny < M:
                    queue.append(((nx, ny), (x, y)))

    return graph

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

# 상하좌우 비교할 때 사용
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

print(bfs(graph)[N-1][M-1]-1)