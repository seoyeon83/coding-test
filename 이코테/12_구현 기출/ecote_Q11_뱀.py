'''
261004 삼성전자 SW 역량테스트 기출 

Dummy 도스 게임
사과를 먹으면 뱀 길이 증가
뱀 자신의 몸 or 벽에 부딪히면 게임 종료

N * N 보드, 몇몇 칸에 사과. 보드 끝에는 벽 존재
시작할 때 1, 1 에 존재하고 길이는 1, 방향은 오른쪽

- 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다
- 이동한 칸에 사과가 있다면 사과는 없어지고 꼬리는 움직이지 않는다 (길이가 늘어난 채로 유지되니까)
- 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비운다

사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는 지를 계산하라

N, K
사과 위치 (행, 열)
뱀위 방향 변환 횟수 L
X, C ... 게임 시작 시간으로부터 X초가 끝난 뒤 왼 L or 오 D로 90도 방향을 회전시킨다
X는 게임이 시작한 후 X초가 지났다는 뜻
여기서 중요한 건 뱀은 매 초마다 이동하는데, 문제에서 주어지는 X초마다 방향을 바꾼다는 것

예제:
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
=> 9

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
=> 21

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
=> 13
'''

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) 
K = int(sys.stdin.readline().rstrip())
apples = set(tuple(map(int, sys.stdin.readline().split())) for _ in range(K))
L = int(sys.stdin.readline().rstrip())
directions = deque()
for _ in range(L):
    X, C = sys.stdin.readline().split()
    directions.append((int(X), C))

snake = deque([(1, 1)])
d, x, y, answer = 0, 1, 1, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    answer += 1

    # 다음 위치 계산
    nx, ny = x + dx[d], y + dy[d]
    if 1 > nx or nx > N or 1 > ny or ny > N or (nx, ny) in snake:
        break

    # 이동
    x, y = nx, ny
    # print(answer, x, y, snake)
    if (x, y) in apples:
        apples.remove((x, y))
    else:
        snake.popleft()
    snake.append((x, y))

    # 방향 전환
    if directions and directions[0][0] == answer:
        X, C = directions.popleft()
        d = (d-1)%4 if C == 'L' else (d+1)%4
    
print(answer)

'''
메모:
이게 말이 애매해서 그렇게 이동하면서 사과가 있으면 먹고 아니면 말고인 거임

일단 반복문으로 구현해 (while True)
특히 중요한 건 방향 바꾸는 건 X초가 지났을 때. second를 더하고, 방향을 바꾸는 거임
뱀의 몸 길이 좌표는 거꾸로된 queue로 생각해야할 듯
[(1,2)]
[(2,2), (1,2)] -> 이동 + 사과 하나 먹음
[(3,2), (2,2)] -> 이동
[(3,3), (3,2), (2,2)] -> 이동 + 사과 하나 먹음
[(3,4), (3,3), (3,2),] -> 이동
즉 나의 직관대로면 ... queue의 맨 뒤(계속 추가되는 곳, 인덱스 -1)가 뱀의 머리(x,y)고 맨 앞(빠지는 곳, 인덱스 0)이 뱀의 머리인 것
queue로 하면 in으로 O(N)이 되긴 하지만 이동할 곳이 뱀의 몸과 충돌하는지도 알 수 있으니까 deque를 활용해야겠음
근데 이걸 그래프로 하는 게 의미가 있나?

queue 정의 (시작은 0, 0)
d는 동쪽
dx, dy 정의 (0:동, 1:남, 2:서, 3:북) D면 +1, L이면 -1하면 됨 (%4)
while True:
    다음 이동할 좌표 계산
    if 벽이나 자기 몸에 부딪히나? -> break, 현재 시간 체크
    시간 계산 + 1
    만약 이동할 곳에 사과가 없으면 pop하고 push,
    아니면 push만
    방향 전환 (L이면 왼, D면 오)

근데 N * N 맵이랑 사과 위치를 그래프로 2차원 배열로 만들 필요가 있을까? 난 모르겠는데 애초에 뱀을 queue로 표현하는 건데 사과 위치때문에?
굳이?
근데 고민인 게 사과를 리스트로 해서 이걸 먹을 때 remove 시켜버리면 너무 비효율적인 연산이 될 것 같.. 잠만.. set으로 하면 되잖아?
그리고 뱀 방향 전환은 시간 순으로 주어지므로 deque로 선입선출 시키자.. 아니면 dict로 초별로 ? 아니야 그냥 deque로 해서 [0] 으로 확인하고 pop시키자

회고:
아 내가 문제에서 주어지는 값들이 모두 1-index 라는 걸 간과했구나.. 그래서 디버깅하느라 30, 40분이면 끝낼 수 있던 걸 56분이 걸렸다 ㅠㅠ
그래도 빠르게 문제를 파악해서 로직을 옮게 짰다는 점.. 중간중간 비용을 판단한 것들이 맞게 잘 생각했다는 점이 아주 만족스럽다
특히 사과 위치, 방향 전환 정보, 뱀 위치를 저장하는 변수 자료구조를 적재적소로 선택한 것을 칭찬하고 싶다.
다음에는 문제를 보고 1-index로 풀 건지, 0-index로 풀 건지 확실히 생각하고 풀어야겠다.
그리고 설계한 걸 코드로 옮기는 과정, 그리고 고치면서 연관된 곳을 놓치는 경우가 많이 보여서 이 부분도 조심해야겠다.
'''