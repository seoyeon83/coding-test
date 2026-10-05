# 연결 요소 찾기: dfs로 같은 값으로 연결된 덩어리 찾고, 그 크기를 세는 템플릿
# 재귀가 길어질 수 있다면 스택을 쓴다 (더 안전)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 연결된 영역 크기 세기
# 이때 visited는 set()이 아니라 bool 원소를 담은 2차원 리스트
def dfs_stack(grid, sr, sc, visited):
    n, m = len(grid), len(grid[0])
    target = grid[sr][sc]       # 시작 칸의 값 = 이 덩어리의 값 (즉, 특정 색이나 값을 갖는 덩어리만 세어야 하는 경우)
    stack = [(sr, sc)]
    visited[sr][sc] = True      # 시작점 방문 처리
    size = 0

    while stack:
        r, c = stack.pop()
        size += 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc]:
                continue
            if grid[nr][nc] != target:
                continue
            # 방문 처리 (순서가 중요하지 않아서)
            visited[nr][nc] = True
            stack.append((nr, nc))
    return size

# grid를 순회
def count_regions(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    sizes = []
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and grid[r][c] != 0:
                sizes.append(dfs_stack(grid, r, c, visited))