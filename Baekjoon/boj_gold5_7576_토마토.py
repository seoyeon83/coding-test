'''
익은 토마토 왼오앞뒤 네 방향에 있는 토마토들이 영향을 받아서 익게 됨
며칠이 지나면 다 익게 되는지 최소 일수
1은 익은, 0은 익지 않은, -1은 없는 것

모두 익지 못하는 상황이면 -1을 출력
저장될 때부터 모든 토마토가 익어있으면 0 출력

익은 토마토에서 bfs로 ()

메모리초과..............? 시간 초과.........?
기존 코드에서 원래는 방문 처리를 노드에서 값을 꺼낼 때 최단 거리를 갱신하도록 했는데
큐에 값을 넣을 때 최단거리를 갱신하는 방식으로 바꿈
큐에 넣는 시점에 바꾸는 것이라.. 익은 토마토가 동일한 좌표를 탐색할 때 이미 큐에 들어가 있는 좌표임에도
큐에 다시 넣게될 수가 있음!!!!!!!!!!!!!!!!!! 
'''

# import sys 
# from collections import deque


# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]


# M, N = map(int, sys.stdin.readline().split())
# tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# # 만약 모두 익어있다면
# temp = 0
# for x in range(N):
#     for y in range(M):
#         temp += tomatos[x][y]
# if temp == M * N:
#     print(0)
#     sys.exit(0)

# # 탐색
# # 익은 토마토의 좌표를 미리 queue에 넣기
# queue = deque()
# for x in range(N):
#     for y in range(M):
#         if tomatos[x][y] == 1:
#             queue.append([x, y, 1])

# while queue:
#     x, y, distance = queue.popleft()
#     if tomatos[x][y] > -1:
#         tomatos[x][y] = distance + 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M \
#                 and (tomatos[nx][ny] == 0 or tomatos[nx][ny] > (tomatos[x][y] + 1)):
#                 queue.append([nx, ny, tomatos[x][y]])


# # 모두 익을 수 없는 경우와 최댓값(정답) 탐색
# answer = -1
# for x in range(N):
#     for y in range(M):
#         if tomatos[x][y] == 0:
#             print(-1)
#             sys.exit(0)
#         if tomatos[x][y] > answer:
#             answer = tomatos[x][y]


# print(answer-2)

import sys
from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


M, N = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 만약 모두 익어있다면
temp = 0
for x in range(N):
    for y in range(M):
        temp += tomatos[x][y]
if temp == M * N:
    print(0)
    sys.exit(0)

# 탐색
# 익은 토마토의 좌표를 미리 queue에 넣기
queue = deque()
for x in range(N):
    for y in range(M):
        if tomatos[x][y] == 1:
            queue.append([x, y])

while queue:
    x, y = queue.popleft()
    if tomatos[x][y] > -1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M \
                and (tomatos[nx][ny] == 0 or tomatos[nx][ny] > (tomatos[x][y] + 1)):
                queue.append([nx, ny])
                tomatos[nx][ny] = tomatos[x][y] + 1


# 모두 익을 수 없는 경우와 최댓값(정답) 탐색
answer = -1
for x in range(N):
    for y in range(M):
        if tomatos[x][y] == 0:
            print(-1)
            sys.exit(0)
        if tomatos[x][y] > answer:
            answer = tomatos[x][y]


print(answer-1)