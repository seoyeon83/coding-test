'''
bfs로 최단 거리를 구하는 전형적인 문제

도착할 수 없는 경우는 -1
갈 수 있는 곳은 1
벽은 0

캐릭터는 좌측 상단 0, 0
상대 진영(도착지)는 n-1, m-1

탐색 후 n-1, m-1 가 1이면, -1 리턴
n과 m 모두 1인 경우는 없으므로 2, 1이 들어왔을 때 적어도 도착지의 값은 2 이상이어야 함

'''
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if nx == 0 and ny == 0: continue
                
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1