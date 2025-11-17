'''
RGB
적록색약인 사람은 R, G를 같은 걸로 보고
아닌 사람은 R, G를 다른 걸로 본다
구역 구하기 (dfs로)

dfs로 순회해서 구역 개수 구하기
변수 하나에 저장해서 하기에는 방문한 경우를 값 변경을 통해 진행하려고 했기 때문에 적록색약인 경우와 아닌 경우로 나눴음
적록색약인 경우는 R, G를 구분 못하므로 하나의 값으로 통일함
'''


import sys


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, area, target):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if area[x][y] in ('R', 'G', 'B'):
            area[x][y] = 'E'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and area[nx][ny] == target:
                    stack.append((nx, ny))


### 재귀함수로 짠 경우 => 재귀함수 호출 횟수 관련 RecursionError가 발생해서 반복문 + 리스트를 사용하는 구현 방식으로 변경
# def dfs(x, y, area, target):
#     # 방문처리
#     area[x][y] = 'E'

#     # 상하좌우 검사 및 호출
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < N and 0 <= ny < N and area[nx][ny] == target:
#             dfs(nx, ny, area, target)


N = int(sys.stdin.readline())
area1, area2 = list(), list()
for _ in range(N):
    inp = sys.stdin.readline().strip()
    area1.append(list(inp))
    area2.append(list(inp.replace('R', 'G')))


# 적록색약 X
cnt = 0
for x in range(N):
    for y in range(N):
        if area1[x][y] in ('R', 'G', 'B'):
            dfs(x, y, area1, area1[x][y])
            cnt += 1

print(cnt, end=' ')

# 적록색약 O 
cnt = 0
for x in range(N):
    for y in range(N):
        if area2[x][y] in ('G', 'B'):
            dfs(x, y, area2, area2[x][y])
            cnt += 1

print(cnt)