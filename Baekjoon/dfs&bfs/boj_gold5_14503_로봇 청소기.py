'''
로봇 청소기와 방의 상태가 주어졌을 때 청소하는 영역의 개수

N * M
벽 또는 빈칸
청소기는 동서남북으로 바라봄
각 칸은 좌표 r,c (0,0) ~ (N-1, M-1)

1. 현재 ㅋ ㅏㄴ이 아직 청소되지 않은 경우, 현재 칸을 청소
2. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 
    a. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 1칸 후진, 아니면 1번으로 돌아간다
    b. 바라보는 방향 뒤쪽 칸이 벽이라 후진할 수 없으면 작동을 멈춘다
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    a. 반시계 방향으로 90도 회전
    b. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 칸인 경우 한 칸 전진
    c. 1번으로 돌아간다

bfs로 하면 될 것 같은데.. 

0은 북, 1은 동, 2는 남, 3는 서
0은 청소 안됨, 1은 벽

반시계로 돌 때: 북서남동
0 -> 3 -> 2 -> 1 -> 0 -...

후진할 때: 남 <-> 북, 동 <-> 서
0 -> 2, 2 -> 0, 1 -> 3, 3 -> 1

현재 칸 청소 -> 방문 처리(2로 값 수정)
주변 네 칸 중 청소되지 않는 칸 찾아보기
-> 없으면 후진... -> 큐에 넣기
-> 뒤쪽이 벽이면 작동 멈추기
청소되지 않은 빈 칸이 있기만 해도 반시계 방향으로 90도 회전(북->서->남->동)
앞쪽 칸이 청소되지 않으면 한 칸 전진 -> 큐에 넣기
앞쪽 칸이 청소되지 않았으면 다시 90도 돌기(그 청소되지 않은 칸이 보일 때까지 도는 거임)
'''

### 1차적으로 짠 코드 -> 통과
import sys
from collections import deque

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(x, y, d):
    cnt = 0
    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        if graph[x][y] != 1:
            # 청소 및 카운트
            if graph[x][y] == 0:
                graph[x][y] = 2
                cnt += 1

            # 주변에 있는지 확인
            flag = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= N and 0 <= ny <= M and graph[nx][ny] == 0:
                    flag = True
                    break

            # 주변에 있으면
            if flag:
                # 방향 전환하며 청소되지 않는 칸 찾기
                for _ in range(4):
                    d = d-1 if d > 0 else 3
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx <= N and 0 <= ny <= M and graph[nx][ny] == 0:
                        queue.append([nx, ny])
                        break

            # 주변에 없으면
            else:
                i = d-2 if d > 1 else d+2
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= N and 0 <= ny <= M and graph[nx][ny] != 1:
                    queue.append([nx, ny])
                elif graph[nx][ny] == 0:
                    return cnt

    return cnt

print(bfs(r, c, d))


### 깔끔하게 로직 수정
import sys
from collections import deque

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

while True:
    # 청소 및 카운트
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1

    # 주변에 있으면
    flag = False
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dx[d]
        nc = c + dy[d]

        # 방향에 청소하지 않은 공간이 있다면
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
            r, c = nr, nc
            flag = True
            break # 1번부터 다시 시작

    # 주변에 없으면
    if not flag:
        bd = (d - 2) % 4
        br = r + dx[bd]
        bc = c + dy[bd]

        # 후진할 수 있다면 
        if 0 <= br < N and 0 <= bc < M and graph[br][bc] != 1:
            r, c = br, bc 
        # 후진할 수 없으면 정지
        else:
            break  

print(cnt)