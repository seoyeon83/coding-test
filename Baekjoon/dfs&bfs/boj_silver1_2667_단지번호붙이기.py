'''
인접한 단지별로 같은 번호 부여
1은 집, 0은 집 아님
단지별 집 개수 출력 

상하좌우 dfs 순회 재귀로 구현하자 
한 번 순회 다 하면서 단지 하나
(x, y) 

이건 그동안 돌던 인접 리스트 그래프가 아니라 배열 형식 



'''
import sys


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문한 개수 반환(visited 개수 반환)
def dfs(x, y):
    visited = set()
    stack = [(x, y)]
    cnt = 0

    while stack:
        # print(stack)
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            cnt += 1
            graph[x][y] = 0  # 0으로 만들어서 탐색 못하게 하기 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (nx, ny) not in visited and nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] > 0:
                    stack.append((nx, ny))
    
    return cnt

N = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

# 단지별 집 수를 결과 리스트에 저장
ans = list()
for x in range(N):
    for y in range(N):
        if graph[x][y] > 0:
            ans.append(dfs(x, y))

ans.sort()

print(len(ans))
for a in ans:
    print(a)