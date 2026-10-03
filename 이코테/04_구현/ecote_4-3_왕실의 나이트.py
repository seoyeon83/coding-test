'''
261003

8 * 8 (1~8, a~h)
특정 한 칸에 나이트 존재, L자 형태로만 이동 가능/
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

나이트 위치가 주어졌을 때 이동할 수 있는 경우의 수 출력
왜냐면 위치에 따라 판 밖으로 나갈 수도 있으니까

a1 이런식으로 입력됨 -> 2

근데 입력은 a1 이렇게 되는데 결국 계산하기 편하게 하려면 a ~ h를 1~8로 변환해야 함
그리고 경우의 수만 찾는 거라 다시 알파벳으로 롤백할 필요가 없다
ord('a') - 96 = 1
'''

import sys

values = sys.stdin.readline()
x = int(values[1])
y = ord(values[0]) - 96

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        answer += 1

print(answer)

# 개선: 96 대신 ord('a') 활용, 그리고 dx와 dy를 묶는 방식 (개수가 많아지면 묶는 게 좋다), rstrip() 추가
import sys

values = sys.stdin.readline().rstrip()
x = int(values[1])
y = ord(values[0]) - ord('a')

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
answer = 0
for dx, dy in steps:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        answer += 1

print(answer)