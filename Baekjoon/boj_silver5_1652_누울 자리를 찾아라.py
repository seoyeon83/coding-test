'''
연속한 2칸 이상의 빈 칸
가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램
어쨌든 칸 수는 2칸 이상으로 연속하기만 되는 거네
이걸 dfs로 해야하나...
각 방향대로 칸별로 탐색 진행. 방문한 경우는 값을 바꿔서 체크
근데 그냥 탐색을 꼭 해야하나?

각 세로, 가로 방향 별로 변수를 따로 저장
X로 split한 뒤에 길이가 2 이상인 것만 카운트하면 되잖아?


'''

import sys 


N = int(sys.stdin.readline())
room = [list(sys.stdin.readline().strip()) for _ in range(N)]
# 세로 방향으로
room_r = [list(row) for row in zip(*room)][::-1]

# 가로 방향 확인
a = 0
for row in room:
    row = ''.join(row).split('X')
    for r in row:
        if len(r) > 1:
            a += 1

print(a, end=' ')

# 세로 방향 확인
b = 0
for row in room_r:
    row = ''.join(row).split('X')
    for r in row:
        if len(r) > 1 :
            b += 1

print(b, end=' ')