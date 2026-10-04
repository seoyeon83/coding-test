'''
261004 삼성전자 SW 역량테스트 기출 

N * M 연구소, 0: 빈칸, 1: 벽, 2: 바이러스
바이러는 2 ~ 3개, 빈칸은 3개 이상, 벽도 이미 여럿 있음
일부 칸에 바이러스 존재 -> 상하좌우로 인접한 빈칸으로 퍼지기 가능
새로 세울 수 있는 벽의 개수는 3개 (이상도 이하도 안됨 꼭 3개)
벽을 세운 뒤 바이러스가 퍼질 수 없는 칸의 개수를 안전영역의 크기는 그 개수가 됨
안전 영역 크기의 최댓값을 구해야 한다

예제: 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''

import sys
from itertools import combinations

# 디버깅용, 제출할 때는 지우기
def print_graph(g):
    for x in g:
        for y in x:
            print(y, end=' ')
        print()

# 2차원 리스트 복사
# 개선점: 따로 함수로 만들지 않고도 [row[:] for row in graph] 로 할 수도 있다
def copy_graph(g):
    new_g = []
    for x in g:
        new_g.append(x.copy())
    return new_g

# 재귀로 dfs 구현한 버전
# def dfs(x, y):
#     # 안되는 경우
#     if x < 0 or x >= N or y < 0 or y >= M or graph_copy[x][y] in (1, 3):
#         return
#     graph_copy[x][y] = 3
#     dfs(x - 1, y)
#     dfs(x + 1, y)
#     dfs(x, y - 1)
#     dfs(x, y + 1)
#     return 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 개선점: 바이러스인데 방문했던 곳 을 표기하기 위해 3을 정의했는데, 새롭게 상태 정의할 필요 없이 빈칸만 돌도록 조건을 만들면 더 깔끔해진다
def dfs(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if graph_copy[x][y] in (0, 2):
            graph_copy[x][y] = 3
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and graph_copy[nx][ny] in (0, 2):
                    stack.append((nx, ny))

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 빈 칸과 바이러스 위치 찾기
empty, virus = [], []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            empty.append((x, y))
        elif graph[x][y] == 2:
            virus.append((x, y))

# 벽 3개 올릴 위치 선정해서 바이러스 시뮬레이션
answer = 0
for comb in combinations(empty, 3):
    graph_copy = copy_graph(graph)
    for x, y in comb:
        graph_copy[x][y] = 1
    for x, y in virus:
        dfs(x, y)

    # 빈 칸(안전 영역) 크기 세기
    # 개선점: sum(row.count(0) for row in graph_copy) 로 줄이기 가능
    cnt = 0
    for x in range(N):
        for y in range(M):
            if graph_copy[x][y] == 0:
                cnt += 1

    # 개선점:  answer = max(answer, cnt) 로 줄이기 가능
    answer = cnt if cnt > answer else answer

print(answer)

'''
메모:
1. 벽을 세울 위치 선정
    먼저 빈칸의 위치, 바이러스 위치를 계산한다
    빈칸의 위치 중 3개를 선정한다 (itertools.combinations)
2. bfs/dfs로 바이러스 퍼지게 하기
    선정한 위치에 벽을 두고 바이러스가 퍼지게 한다
3. 안전영역 개수 세고, 앞서 센 값과 비교해서 최댓값이면 저장

이때 조심해야할 건 초기 입력값을 그대로 두고 벽 3개 설정 + 탐색을 돌려야 한다는 점
그러면 반복할 때마다 ..,. copy를 해야 하나?

아 이게 너무 헷갈리고 어려운 게 방문 처리랑 바이러스랑 좀 다른데? 3으로 할까?

회고:
42분이라는 시간 동안 내가 짠 코드의 문제점을 파악해서 결국 문제를 풀 수 있었다! (권장 풀이 시간이 40분이었으니.. 꽤나 준수해졌다)
중간에 2차원 리스트에서 안쪽에 있는 리스트는 단순히 copy()로 전체 복사가 되지 않는다는 점, 내가 짠 dfs 로직에 문제가 있었다는 점이 가장 큰 문제였다.
특히 두 번째는 내가 dfs를 짜면서 2(바이러스)가 두 가지 의미를 가지면서 방문 처리가 꼬였다는 점이었다. 
바로 생각한 해결책은 3이라는 상태값을 추가해서 바이러스인데 방문한 노드를 표기하도록 하면서 해결할 수 있었다.
초반에 문제 풀이 설계를 빠르게 한 덕분에 중후반부에 이 두 문제를 디버깅할 수 있었다.
코드를 돌아보니 더 깔끔하게 한 줄로 표현할 수 있던 부분들이 있어서 이 부분은 꼭 기억해뒀다가 다음에 풀 때 활용해 볼 것이다.
'''