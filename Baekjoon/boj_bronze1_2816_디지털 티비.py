'''
kbs1, kbs2
리스트 순서를 바꿔서 kbs1, kbs2, 나머지 ... << 형태로 만들어라
리스트 왼편에 작은 화살표.. 이게 현재 선택한 채널을 나타내는 것. 제일 첫 번째 채널을 가리키는 것

1번: 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
2번: 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
3번: 현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
4번: 현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

일단 이것만 구현 -> kbs1을 찾고 올리고, kbs2를 찾고 올리고

2,3번 버튼을 쓰지 않아도 통과가 된다
왜냐면 스페셜 저지 문제이고 1, 4만 사용해도 문제의 제한 안에는 충분히 들어가기 때문!
최소한으로 움직여야 하는 문제가 아니기 때문
'''

import sys 

N = int(sys.stdin.readline())
channels = [sys.stdin.readline().strip() for _ in range(N)]

# kbs1을 찾는다
target = 0
while channels[target] != "KBS1":
    print(1, end='')
    target += 1
# kbs1을 끌어올린다
while channels[0] != "KBS1":
    print(4, end='')
    channels[target], channels[target-1] = channels[target-1], channels[target]
    target -= 1

# kbs2를 찾는다
while channels[target] != "KBS2":
    print(1, end='')
    target += 1
# kbs2을 끌어올린다
while channels[1] != "KBS2":
    print(4, end='')
    channels[target], channels[target-1] = channels[target-1], channels[target]
    target -= 1