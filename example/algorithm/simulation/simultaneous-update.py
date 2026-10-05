# 시뮬레이션, 동시에 일어나는 변화 새 배열에 쓰기
# 예: 미세먼지 확산, 각 칸의 먼지가 양의 1/5씩 인접 칸으로 퍼지고 퍼진 만큼 원래 칸에서 빠진다

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def spread(grid):
    n, m = len(grid), len(grid[0])
    new = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if grid[r][c] <= 0:
                new[r][c] += grid[r][c]     # 벽(-1) 등 유지
                continue
            amount = grid[r][c] // 5
            cnt = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != -1:
                    new[nr][nc] += amount
                    cnt += 1
            # 퍼진 만큼 원래 칸에서 빼기
            # += 인 이유는 여러 칸에서 퍼질 수도 있으므로 여러 곳에서 모이므로 +=
            new[r][c] += grid[r][c] - amount * cnt
    return new