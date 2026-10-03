'''
N * M, 각각 칸은 육지 or 바다
각 칸은 A, B로 표현 가능
A: 북쪽으로부터 떨어진 칸의 개수
B: 서쪽으로부터 떨어진 칸의 개수 -> 이거 그냥 인덱스네

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전)부터 차례대로 갈 곳을 정한다
2. 왼쪽 방향에 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 뒤 전진. 가보지 않은 칸이 없다면 1단계로 돌아간다
3. 네 방향 모두 가본 칸이거나 바다로 된 경우는 바라보는 방향을 유지한 채로 한 칸 뒤로 이동하고 1단계로 돌아간다. 뒤쪽이 바다면 멈춘다 

각 동작은 결국 3단계에서 뒤쪽이 바다여야 멈춘다
dfs/bfs 생각나는데...
육지인데 간 곳은 -1로 표기하자
'''

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
# 0: 북, 1: 동, 2: 남, 3: 서 (시계방향, 왼쪽 방향으로 돌릴 때는 -1을 해줘야 함)
A, B, d = map(int, sys.stdin.readline().rstrip().split())
# 0: 육지, 1: 바다
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
graph[A][B] = -1
# 북 동 남 서 순서
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]
answer = 1
flag = 0
while True:
    # print(A, B, d, flag)
    if A < 0 or B < 0:
        break
    # 사방 중에 방문하지 않은 육지가 없는 경우 (모두 -1, 1인 경우)
    if flag > 3:
        nd = (d-2)%4
        nx, ny = A + dx[nd], B + dy[nd]
        # 뒤쪽이 바다인 경우 (범위를 벗어나거나, 바다인 경우)
        if (1 <= nx <= N and 1 <= ny <= M and graph[nx][ny] == 1) \
            or nx < 1 or nx > N or ny < 1 or ny > M:
            break

        # 후진
        A, B = nx, ny
        flag = 0
        continue

    # 1. 왼쪽 방향이 갈 수 있는지 탐색 (가보지 않은 육지인가?) 
    d = (d - 1)%4
    nx, ny = A + dx[d], B + dy[d]
    # 2. 갈 수 있다면 전진 (회전, 직진)
    if 1 <= nx <= N and 1 <= ny <= M and graph[nx][ny] == 0:
        A, B = nx, ny
        graph[A][B] = -1
        answer += 1
        flag = 0
    # 갈 수 없는 경우
    else: 
        flag += 1
    

print(answer)