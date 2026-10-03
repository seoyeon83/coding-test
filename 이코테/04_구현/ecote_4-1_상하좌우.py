'''
L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

도착 지점 좌표 (공백 두고)
좌표는 1~N (0-index 아님)
'''

# 261003 1차 풀이
import sys

N = int(sys.stdin.readline())
commands = sys.stdin.readline().split()

idx = {'L':0, 'R':1, 'U':2, 'D':3}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1
for command in commands:
    if 0 < x + dx[idx[command]] <= N and 0 < y + dy[idx[command]] <= N:
        x += dx[idx[command]]
        y += dy[idx[command]]

print(x, y)

# 개선: 변수 정의하는 걸 활용해서 더 가독성 좋게 구현

import sys

N = int(sys.stdin.readline())
commands = sys.stdin.readline().split()

idx = {'L':0, 'R':1, 'U':2, 'D':3}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1
for command in commands:
    d = idx[command]
    nx, ny = x + dx[d], y + dy[d]
    if 1<= nx <= N and 1<= ny <= N:
        x, y = nx, ny

print(x, y)