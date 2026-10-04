'''
261004 삼성전자 SW 역량테스트 기출 

N * N
나라가 하나씩 존재
r행 c열 나라에 A[r][c] 명이 살고 있다
인접한 나라 사이에 국경선이 존재

인구 이동
- 국경선을 공유하는 두 나라(인접한 나라)의 인구 차이가 L명 이상, R명 이하라면, 국경선 오픈
- 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면 인구 이동 시작
- 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 하루 동안 연합이라고 한다
- 연합을 이루고 있는 각 칸의 인구수는 (연합 인구수) / 칸의 개수(국가 개수)가 된다 (소수점 버림)
- 연합을 해체하고 모든 국경선을 닫는다

즉, 인구 차이를 X라고 할 때 L <= X <= R 이면 국경선 오픈 -> 그 국경선은 인구 이동 가능

각 나라의 인구수가 주어졌을 때 인구이동이 몇 번 발생하는가?

예제:
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
=> 3

3 5 10
10 15 20
20 30 25
40 22 10
=> 2

2 20 50
50 30
30 40
=> 1
'''


import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
while True:
    # 연결 리스트 계산
    line = {}

    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    if (x, y) not in line.keys(): line[(x, y)] = {(nx, ny)}
                    else: line[(x, y)].add((nx, ny))
                    if (nx, ny) not in line.keys(): line[(nx, ny)] = {(x, y)}
                    else: line[(nx, ny)].add((x, y))
    # 연결 리스트가 비었다면 더이상 인원 이동 불가
    if not line: break

    # 연결 리스트 기반 bfs 탐색으로 연합의 인구 수 및 개수 측정 -> 인구 수 계산 및 업데이트
    #   line으로 인접한 노드들을 찾아서 list에 저장. 개수 및 인구 수 합 측정 -> 계산해서 graph에 업데이트
    #   근데 고민인 건 bfs를 여러 번 돌려야 하는데 이미 방문한 곳일 수 있다. visited 추가해야겠다
    visited = set()
    for x, y in line.keys():
        if (x, y) not in visited:
            queue = deque([(x, y)])
            visited.add((x, y))
            cnt = [graph[x][y]]
            point = [(x, y)]
            while queue:
                x, y = queue.popleft()
                for nx, ny in line[(x, y)]:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        cnt.append(graph[nx][ny])
                        point.append((nx, ny))
            # 국가별 인구 수 업데이트
            avg = sum(cnt) // len(cnt)
            for i, j in point:
                graph[i][j] = avg
    answer += 1

print(answer)


'''
메모: 
이게 인구이동이 며칠동안 일어나는 거네... 인구이동이 없을 때까지, 즉 인구 차이가 L명 이상, R명 이하가 되지 않을때까지 하는 거네
계속해서 연합해서 인구수를 공평하게 나눠 가지게 되니까 결국에는 인구 차이가 L명 미만이 될 때까지 진행하는 거네.. 이제 이해했다

흠 그러면 이게.. 단순 격자로 하는 게 아니고 각 노드 간 연결이 되느냐가 문제네
한 번 격자를 돌면서 인구 수 차이를 파악하고, 그 차이를 기반으로 연결 리스트를 만들어야겠네
그럼 연결리스트를 만들면 연합이 나오겠지. 그럼 각 연합의 인구 수를 다 합쳐서 개수만큼 나누고, 그래프의 인구수를 업데이트한다
근데 더이상 인구이동이 없다는 걸 파악하려면? 인구이동이 더 없는 경우는.. N개 국가가 모두 인원 수가 같아졌거나 (L 미만), 그 차이를 더이상 메꿀 수 없을 때임(R 초과)
그러면 인접 리스트가 빈 값이면 되겠네

answer = 0
while True:
    1. graph를 순회하면서 국가 간 인구 수 차이를 기반으로 연결 리스트를 만든다 
        이때 연결 리스트가 빈 값이면 break 한다
    2. 연결 리스트를 bfs?dfs? 탐색해서 연합의 인구 수와 개수를 측정 -> 인원 이동 후 인구수 계산
    3. graph 업데이트
    answer += 1

뭔가 잘못됐다.. 탐색 부분이 뭔가 크게 잘못됐다

회고:
연결 리스트를 따로 만들 필요 없이 BFS 만으로 풀이가 가능했는데 이걸 처음에 생각하지 못한 점이 아쉬웠다
40분 짜리 문제였는데 이번에도 BFS 내 로직 문제로 시간을 좀 초과해서 52분만에 풀었다
문제를 풀면서 수월하다는 감각이 없어서 앞서 푼 두 문제보다 상당히 초조해하며 풀어서 그런지 변수명이나 보다 깔끔하게 구현하지 못한 포인트들도 아쉬웠다.
예를 들어 point, cnt 둘 다 안 써도 point만 썼어도 충분했을 것이라는 점..
그래도 한동안 어려운 코테 문제를 안 풀어왔던 것 치고, 너무 졸린 밤에 푼 것이라는 것 치고 1시간 안에 로직은 정답인 코드를 작성했다는 점은 아주 긍정적이다! (비록 시간 초과가 날 수는 있지만..)
'''