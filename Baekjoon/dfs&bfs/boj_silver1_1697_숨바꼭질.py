'''
수빈 -> N / 동생 -> K
수빈이 위치가 X면 1초 후 X-1 or X+1로 이동하게 됨
순간이동 -> 1초 후에 2*X의 위치로 이동

1차원인가본데?

수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인가?

dfs로?
bfs로 하는 게 낫다.. 한 가지를 끝까지 파고드는 것보다 모든 이동이 1초로 동일하므로 bfs로 찾는 것이 정석이다는 것
bfs로 현재 값이 K인지 확인 후, 세 가지 경우(x-1, x+1, x*2)에 대해 탐색 진행
이때 이동에 대해서 함께 저장

근데 메모리 초과.......?

=> gemini와 함께 풀었는데...
visited 배열로 각 좌표에 대해서 방문했는지 아닌지 검사
원래는 x랑 time을 같이 저장하도록 했었는데 그러니 메모리 초과가 발생했었음
y를 구한 뒤 K와 검사하는 것과 visited에 방문 표시를 하는 걸 큐에 넣어서 다음 while 반복에서 진행하는 게 아니고..
queue에 넣을 때 같이 진행함
그리고 x의 범위에 대해서도 최적화 진행
아,,, 최적화하기가 어렵네 ㅜㅜ
'''

import sys
from collections import deque


def bfs(N, K):
    if N == K: return 0

    queue = deque([[N, 0]])
    visited = [False] * 100001
    visited[N] = True

    while queue:
        x, time = queue.popleft()

        for y in (x-1, x+1, x*2):
            if 0 <= y <= 100000 and not visited[y]:
                if y == K: return time + 1
                visited[y] = True
                queue.append([y, time+1])


N, K = map(int, sys.stdin.readline().split())

print(bfs(N, K))