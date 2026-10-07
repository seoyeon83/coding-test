'''
261007 코드트리 / 삼성 2025 상반기 오후 1번 미생물 연구
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description

N * N 배양 용기, 이때 좌측 하단이 (0, 0), 우측 상단이 (N, N)
총 Q번의 실험을 진행하며 각 실험 결과 기록

1. 미생물 투입
    - 좌측 하단 좌표가 (r1, c1) 이고 우측 상단 좌표가 (r2, c2)인 영역에 미생물 투입
    - 영역 내 다른 미생물이 존재하면 새로 투입된 게 잡아먹음 (모든 영역에는 새로 투입된 것만)
    - 기존에 있던 미생물 무리 A가 새로 투입된 B에게 잡아먹히면서, 
      A가 차지한 영역이 둘 이상으로 나눠지게 되면 A 무리의 미생물은 배양용기에서 모두 사라진다
      => 미생물 무리는 무조건 하나여야 한다는 것. bfs 써야하는 지점인듯
2. 배양 용기 이동
    - 모든 미생물을 새로운 배양 용기로 이동시킨다. 새 배양 용기의 크기도 기존 용기와 동일
      (이건 기존용기에 한 마리도 존재하지 않을 때까지 다음 작업을 반복하는 것으로 진행됨)
    - 기존 배양 용기 무리 중 가장 넓은 무리를 하나 선택(둘 이상이면 먼저 투입된 것 선택)
    - 선택된 무리를 새 배양 용기에 옮긴다
    - 기존 형태를 유지하면서 미생물 무리가 차지한 영역이 배양 용기를 벗어나지 않고 
        다른 미생물의 영역과 겹치지 않아야 함. 
        즉, 위치가 100% 똑같아야하는 건 아닌데 형태가 유지되어야 하나 봄
        최대한 x 좌표(c)가 작은 위치로 미생물을 옮겨야 하고, 
        그런 위치가 둘 이상이면 y좌표(r)가 작은 위치로 오도록
3. 실험 결과 기록
    - 미생물 무리 중 상하좌우로 맞닿은 면이 있는 무리끼리는 인접한 무리라고 표현
    - 모든 인접한 무리 쌍 확인 (a, b)
    - 확인하는 두 무리가 a, b면 a넓이 * b넓이 만큼 성과 얻기
    - 모든 쌍의 성과를 더한 값이 이실험의 결과 
'''
import sys
from collections import deque 

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# i별 순회 및 방문 표기
def visiting_groups(r, c, j, visited):
    visited[r][c] = True
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not(0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if grid[nr][nc] != j:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))

# 인접한 다른 미생물이 있는지 탐색
def find_neighbors(r, c, j):
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not(0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True

            if grid[nr][nc] == -1:
                continue

            if grid[nr][nc] == j:       # 본인인 경우
                q.append((nr, nc))
                continue

            # 이웃으로 추가
            n = sorted([j, grid[nr][nc]])
            if n not in neighbors:
                neighbors.append(n)


N, Q = map(int, sys.stdin.readline().split())
positions = {i: list(map(int, sys.stdin.readline().split())) for i in range(Q)}
cells = {i:set() for i in range(Q)}            # 현재 미생물별 좌표

grid = [[-1] * N for _ in range(N)]     # 격자

# Q번 실험 진행 
for i in range(Q):
    # 1. 미생물 투입
    r1, c1, r2, c2 = positions[i]
    for r in range(r1, r2):
        for c in range(c1, c2):
            # 덮어 씌워지는 경우 cells 갱신
            if grid[r][c] != -1:
                cells[grid[r][c]].remove((r, c))
            grid[r][c] = i
            cells[i].add((r, c))
    
    # 영역 내 2개 이상으로 나눠진 무리가 있는지 bfs 탐색
    visited = [[False] * N for _ in range(N)]
    existing = set()
    remove_cells = set()
    for r in range(N):
        for c in range(N):
            if grid[r][c] != -1 and not visited[r][c]: # 미생물이 있으면
                if grid[r][c] in existing:     # 이미 탐색한 경우(둘 이상으로 갈라진 경우)
                    remove_cells.add(grid[r][c])
                    continue
                visiting_groups(r, c, grid[r][c], visited)
                existing.add(grid[r][c])
    # 번호 기록한 게 있으면 순회하면서 지우기 (0으로)
    if remove_cells:
        for r in range(N):
            for c in range(N):
                if grid[r][c] in remove_cells:
                    grid[r][c] = -1
        
        # 아예 변수에서 없애기
        for j in remove_cells:
            del cells[j]

    # 2. 배양 용기 이동
    # 0 ~ i까지(존재하는 것만) 중에서 넓이(칸 수), 인덱스 기준으로 정렬하기
    wide = [(j, len(cells[j])) for j in range(i+1) if cells.get(j, 0)]
    wide.sort(key=lambda x: (-x[1], x[0]))
    
    new_grid = [[-1]*N for _ in range(N)]
    flag = False
    for j, _ in wide:           # 미생물 별로 이동
        r, c = min(cells[j])
        for ddr in range(-r, N-r+1): # 목표 r
            for ddc in range(-c, N-c+1):  # 목표 c
                test_grid = [row[:] for row in new_grid]
                new_cells = set()
                for x, y in cells[j]:
                    nr, nc = x + ddr, y + ddc
                    if not(0 <= nr < N and 0 <= nc < N):    # 범위 벗어남
                        break
                    if test_grid[nr][nc] != -1:             # 다른 미생물 침범
                        break
                    test_grid[nr][nc] = j
                    new_cells.add((nr, nc))
                else:                                       # 적절한 위치에 이동시킨 경우
                    flag = True
                    new_grid = test_grid
                    cells[j] = new_cells
                    break
            if flag:
                break
        if flag:
            flag = False
        else: # 아무것도 못 놓은 경우
            del cells[j]
            

    grid = new_grid

    # 3. 실험 결과 기록
    neighbors = []
    for j, _ in wide:
        if j not in cells:
            continue
        r, c = min(cells[j])
        find_neighbors(r, c, j)

    # 계산
    answer = sum(len(cells[neighbor[0]]) * len(cells[neighbor[1]]) for neighbor in neighbors)
    print(answer)


'''
[메모]
문제 길이 자체는 짧은데 복잡하고 까다로워 보인다
Q줄에 걸쳐 추가되는 미생물의 위치가 추가된다
i번째 줄에는 i번째로 추가되는 미생물의 r1, rc, r2, rc가 주어진다

가장 고민인 게 여기는 1사분면?맞나 아무튼 기존에 내 머릿속에 있는 grid랑은 형태가 다름
이걸 어떻게 표현할까? 마치 grid를 왼쪽으로 90도 돌린 느낌이네.. 근데 꼭 맞춰야할 필요가 있을까?
디버깅이 어려울 수는 있겠지만 차라리 그냥 들어오는 값 그대로 저장하는 게 편할 수도 있다. 
r = x, c = y

-1은 빈 공간, 0부터 Q-1까지는 미생물 번호

문제는 미생물이 직사각형이 아니어도 여러 모양을 가질 수 있다는 점이다
이런 상황에서 어떻게 배양 용기를 이동시키지? 
중력 어쩌구 템플릿으로 해봐야 하나? ㅡㄴ데 이건 위험한 게 원래 모양이 흐트러질 수 있음
따라서 원래 미생물의 모양... 즉, 기존 좌표에서 r과 c에 동일하게 같은 값을 더하거나 빼야 한다는 건데
미생물별 뭐 위치는... 좌표를 저장하면 되긴 해. 근데 그게 과연 좋은 방법일까?
bfs 탐색을 활용할 수는 없나? bfs를 탐색할 때 -1만 잡으면 사실 뭐.. 빈 공간도 보여줄 텐데

빈 자리를 꿰차고 들어가야 하는 거잖아? 만약 이미 들어가 있는 게 볼록하거나 불룩한 모양새라면
퍼즐조각처럼 짜맞춰지는 케이스도 없을 거라고 생각할 수 없어 그럼 그 경우까지 어떻게 해야.. 적절한 위치를 찾아
옮길 수 있지?
그리고 정~말 최악의 경우... ㄷ1, 2번째로 넣은 미생물과 그 사이에 미생물 한두칸 짜리가 끼게될 수도 있지 않나?
그러면 그리디? 완전탐색 느낌으로 해봐야 하나? 사실 맨 왼쪽 끝점, 즉 r1, c1 은 쉽게 찾을 수 있을 수도
일단 어떤 케이스든 이미 어떤 미생물들이 들어가 있고 남은 자리에 끼워넣어야 한다고 생각해보자
아 근데 이게 너무 어려운 게 미생물이 울퉁불퉁할 경우까지 고려를 하려고 하니까 ㅈ딘짜 머리 터질 것 같은데?
이걸 결국 떠올리지 못하면 안되는데...ㅠㅠ 아 그ㅜㄴ데 진짜 모르겠어 이거 어떻게 하는 거지?
나의생각을 하나하나 뜯어보자
먼저, x를 결정하려면 나의 높이를 고려해야 함. 
뭔가 그 중력... 그거밖에 생각이 안 나는데 .. 아 근데 그건 아닌 것 같단 말이야.
BFS로 빈 곳을 모두 훑어보고 거기에 끼워맞추기? 아니 이것도 아닌 것 같아.. 

처음에는 단순하게 얘네가 직사각형인 걸로 생각했는데 그렇게 생각하면 안되겠다
미생물별 좌표를 모두 한 번에 저장하게 해야겠어
그리고 이동할 때는 가능한 최소 x, 최소 y를 기준으로 일단 그리드를 채워보고 안되면 넘어가는 식으로 해야겠어

1단계 중:
    # 새로 추가된 거 이전 번호만 탐색을 하는데...
    # visited 로 기록하는데 r, c로 순회하다가 이미 방문한 게 나오면 번호 기록하기
    # i면 0~i-1까지가 범위
    # 이때 bfs는 r, c, i, visited를 받아야 함. 특정 번호만 탐색해야 하니까.
    # bfs 돌리면서 points의 좌표도 지워야 함
    # 만약 r, c에 미생물이 있으면 탐색 후 existing에 기록 -> 다음 좌표에서 미생물이 있는데 이미 기록된 것 -> 넘기기

2단계 중:
    # 정렬 순대로 진행
    # 이때 r과 c가 작은 순서대로 일단 grid에 넣어보고 아니면 취소하고 다음을 테스트하는 식으로 가야 함
    # 울퉁불퉁한 경우도 고려를 해야하므로 완전탐색이라고 생각을 해야 할듯
    # 끝점을 저장하지 않으므로 미리 고려를 할 수 없어서 .. 일단 다 넣어보자 ^^
    # 이때 2중 반복으로 돌 때... 각 변수는 목표 r, c로 하면 애매해진다.
    # 즉, 기존 좌표들에서 얼마를 뺄 것인가. 여야 할 것 같은데?
    # 왜냐면 지금 우리는 기존 미생물들의 위치를 그냥 집합에 저장을 하고 있기 때문에... 아 그냥 왼쪽 끝만 저장을 해둘까?
    # 아니 근데 이게 생각을 해보면 새로 잡히는 위치가 아예 기존 위치보다 r, c 다 증가할 수도 있잖아.
    # 그러면 기존 위치가 r, c고, N=5라고 하면 dr은 (-r ~ N-r), dc는 (-c ~ N-c)가 되어야 하는 거네
    # 근데 사실 각 좌표 위치는 천차만별이고 저것도 범위를 예상할 수 있는 게 아니잖아..
    # 그럼 그 기준점을 왼족 아래 하나 점이 잡는다면? 탐색 범위가 줄어들겠다

3단계 중:
    # 이건 또 어떻게 하지?
    # 상하좌우로 맞닿은 무리 기록하기 - bfs로
    # 실험 기록은 서로 인접한 무리 쌍을 찾기만 하면 된다 {{0,1}, {1, 2}} 이런 식으로
    # bfs 탐색을 하면 되는데.. 미생물별로 돌게 하자. 집합을 반환하도록
    # set() 안에 set()을 넣는 건 안되나봄. 그러면 인접리스트 방식으로 해볼까?
    # 아냐 근데 그것보다는.... 그냥 list 정렬해서 넣자 그건 되겠지
    # 안되는 구나~~~~~~~~~~~ 

[회고]
수행 시간: 251ms, 메모리 24MB

L13은 정말 힘들구나... 순수하게 4시간 이상을 이 문제를 푸는 데 썼다. 

잘한 점:
- 4시간 넘게 막혔는데도 포기하지 않고 끝까지 풀었다
- 핵심 설계 자체는 맞게 했다.
- 긴 반례를 보고 충격적이었지만.. 체계적으로 디버깅해냈다

교훈 / 아쉬웠던 점:

우선 아쉬웠던 점은 처음부터 설계를 자세하게 생각하지 않고 먼저 코드 작성에 들어갔다는 점이다.
이 문제는 레벨이 높은 만큼 복잡하고 세세하게 큰 그림을 잡았어야 했는데,
그렇지 않고 바로 단계별로 작성부터 시작하니까 많이 고쳐야 했다.
많이 막막한 마음에 일단 짜보면 생각이 나지 않을까 했던 건데 꼭 그런 건 아니더라..
심지어 그 과정에서 놓친 문제 조건까지 있었다.
그리고 여전히 오타가 좀 있었다. r, c로 해야하는데 r, r로 해버리는 바람에 상하좌우 탐색 이상해진다던지..
로직은 어떻게 짜더라도 중간중간 버그가 생겨서 더더욱 사전에 꼼꼼히 설계하고 코드를 짜야하는 구나를 실감할 수 있었다.

다음 문제부터는 설계할 때부터 실패하는 경우까지 고려해서 단계별로 적어봐야겠다.
막히면 효율보다도 단순한 방법으로 시간 안에 되는지 계산해 봐야겠다.
'''