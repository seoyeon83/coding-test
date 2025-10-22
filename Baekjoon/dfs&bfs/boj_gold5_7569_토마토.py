'''
M * N * H
보관 후 하루가 지나면 익은 토마토에 인접한 익지 않은 토마토들은 영향을 받아 익게 됨
인접: 상, 하, 좌, 우, 앞, 뒤 
며칠이 지나면 다 익게되는가? (최소 일수)
일부 칸에는 토마토가 들어있지 않을 수도 있다

1: 익은, 0: 익지 않은, -1: 토마토 X 
토마토가 하나 이상 있는 경우만 입력으로 주어진다 (뭔말이지)

토마토가 모두 익지 못하는 상황 -> -1

3차원으로 탐색 어떻게 하묘... 
흠 근데 이게 결국 익는 거라고 하지만 이미 익어있는 토마토로부터 최소 거리를 구하는 것과 마찬가지 아닌가?
익은 토마토로부터 최소거리를 dfs로 구하는 식으로 순회를하고, 나중에 출력할 때 최소값을 찾아서 출력한다
근데 문제는 3차원일 때 어떻게 순회를 할까... 흠 아냐 걍 기존에 해보던대로 하면 쉬울지도?

-> 메인 로직은 잘 생각했으나, 익은 토마토별로 bfs를 수행한다는 건 상당히 좋지 못한 생각이었다 ㅠㅠ
gemini의 힌트로 풀었으니.. 나중에 다시 풀어봐야할듯
'''
import sys 
from collections import deque 

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def bfs(tomatos):
    visited = set()
    queue = deque(tomatos)

    while queue:
        n, p = queue.popleft()
        h, x, y = n
        ph, px, py = p

        if n not in visited:
            visited.add(n)
            # 최단거리 갱신
            if graph[h][x][y] == 0: 
                graph[h][x][y] = graph[ph][px][py] + 1
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i] 
                nh = h + dh[i] 

                if (nh, nx, ny) not in visited \
                and nx >= 0 and nx < N and ny >= 0 and ny < M and nh >= 00 and nh < H \
                and graph[nh][nx][ny] == 0:
                    queue.append([(nh, nx, ny), (h, x, y)])



M, N, H = map(int, sys.stdin.readline().split())
graph = list()
for h in range(H):
    floor = list()
    for n in range(N):
        floor.append(list(map(int, sys.stdin.readline().split())))
    graph.append(floor)

tomatos = list()
for h in range(H):
    for x in range(N):
        for y in range(M):
            if graph[h][x][y] > 0:
                tomatos.append([(h, x, y), (h, x, y)])

bfs(tomatos)

ans = -1
flag = False
for h in range(H):
    for x in range(N):
        for y in range(M):
            if graph[h][x][y] == 0:
                flag = True
            if ans < graph[h][x][y]:
                ans = graph[h][x][y]

if flag:
    print(-1)
else:
    print(ans-1)