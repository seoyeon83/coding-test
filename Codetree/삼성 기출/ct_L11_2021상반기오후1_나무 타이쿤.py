'''
261005 코드트리 / 삼성 2021 상반기 오후 1번 나무 타이쿤
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/description

[문제 요약]
n * n 격자 안에 나무 키우기
서로 다른 높이를 가진 나무들이 주어짐
특수영양제는 1*1 땅에 있는 나무 높이를 1 증가시키고, 씨앗만 있는 경우 높이 1의 나무를 만든다
초기 특수영양제는 n*n 중 좌하던 4개의 칸에만 주어짐

특수 영양제는 이동 규칙이 있다 (따로 주어짐, 이동 방향과 칸 수, 8방향)
이동 방향은 1 ~8까지 동, 북동, 북, 북서, 서, 남서, 남, 동남 순서

겨자의 모든 행, 열은 각각 끝과 끝이 연결되어 있어서 격자 바깥으로 나가면 반대편으로 돌아옴
5*5 일 때 (5, 3) 북동으로 3칸 이동하면 (4, 4), (3, 5), (2, 6) -> (2, 1)이 됨 (6%5)

1년동안 나무 성장 방식
1. 특수 영양제를 이동 규칙에 따라 이동시킨다
2. 영양제 이동 후 해당 땅에 영양제를 투입한다. 투입 후 영양제는 사라지게 된다
3. 영양제 투입한 나무의 대각선으로 인접한 방향에 높이가 1 이상인 나무가 있는 만큼, 
    높이가 더 성장한다. 대각선으로 인접한 방향이 격자를 벗어나는 경우 세지 않음
4. 영양제를 투입한 후 나무를 제외하고,
    높이 2 이상인 나무는 높이 2를 베어 잘라낸 나무로 특수 영양제를 사고, 
    해당 위치에 영양제를 올려둔다  
그럼 그 다음 해는 그 다음 해의 이동 규칙에 따라 이동하면서 이 과정을 반복하데 되는 거지
m년 이후 남아있는 나무의 총 높이의 합을 구하면 된다
'''

import sys
from collections import deque

def count_trees(r, c):
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    trees = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0:
            trees += 1
    
    return trees

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rules = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# 이동 방향 0-index로 변환
for i in range(m):
    rules[i][0] -= 1

# 이동 방향
directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
# 초기 영양제 위치
positions = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])
for year in range(m):
    already = set()
    d, p = rules[year]          # 이번 해의 이동 규칙
    # 1 ~ 2. 영양제를 이동 규칙에 따라 이동시키고 1씩 키우기
    for _ in range(len(positions)):
        # 영양제 이동
        r, c = positions.popleft()
        nr, nc = (r + directions[d][0] * p) % n, (c + directions[d][1] * p) % n
        positions.append((nr, nc))

        # 나무 키우기
        grid[nr][nc] += 1
    
    # 3. 성장한 나무의 대각선 방향 검사 후 1 이상인 나무 개수만큼 키우기
    while positions:
        r, c = positions.popleft()
        cnt = count_trees(r, c)
        grid[r][c] += cnt
        already.add((r, c))

    # 4. 영양제 투입한 나무 제외, 높이 2 이상인 나무는 좌표를 position에 저장하고 2를 뺀다
    for r in range(n):
        for c in range(n):
            # 이미 영양제 투입한 나무면 제외
            if (r, c) in already:
                continue
            
            # 높이 2 이상인 나무
            if grid[r][c] >= 2:
                positions.append((r, c))
                grid[r][c] -= 2


# 남아있는 나무의 총합
# 개선: sum(map(sum, grid)) 이렇게 한 줄로 표현 가능
answer = 0
for r in grid:
    answer += sum(r)

print(answer)

'''
[메모]
일단 0-index로 변환해서 풀 것

일단 문제는 이해했다. 흠.. 
중요한 건 연도별로 반복될 때 영양제 개수 등이 주어지지 않아도 잘 돌아가게 하는 것

year 연도별로 반복

1. 영양제 이동 규칙에 따라 이동시키기
    이때 영양제들 위치를 저장하고 지우기 쉬운 자료구조 필요. queue에 저장하기
    이동 시에는 나머지 연산 활용
2. 해당 땅에 영양제 투입, 영양제 위치 기반으로 격자 위치의 나무 키우기
    이때 위치 기록은 3단계 진행 후 모두 pop해서 없앤다
3. 영양제 투입한 나무의 대각선으로 인접한 방향에 높이가 1 이상인 나무가 있는 만큼 더 성장
    이때 대각선 방향을 모두 검사해서 카운트한 걸 반환하는 함수를 구현하자
4. 영양제 투입한 나무 제외, 높이 2 이상인 나무는 좌표를 position에 저장하고 2를 뺀다

[회고]
처음부터 0-index로 확정해서 구현한 것 (이전에 다른 문제에서 0-index로 했다가 1-index 방식으로 바꾸면서 디버깅에 오래 걸린 적 있음)
단계별로 구현을 고려하면서 영양제 위치(+ 이동한 위치)를 뜻하는 positions를 queue로 설계하고,
성장한 나무 위치는 set()을 따로 저장하면서 비용을 고려해서 자료구조를 잘 선택했다고 생각한다
문제의 요구사항을 잘 고려해서 차분히 풀이해 35분만에 다 풀 수 있었다
단, 영양제의 위치를 생각해 position 이라고 변수를 정했는데 이동한 뒤의 위치도 같은 변수로 처리하면서 가독성이 좀 떨어지게 된 것 같다
이런 부분은 다음에 풀 때 더 조심해야겠다
'''