# 시작점에서 최단거리 (벽은 1, 못가는 칸은 -1)

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(grid, sr, sc):
    n, m = len(grid), len(grid[0])
    # grid에 기록하지 않고 별개로 거리 기록
    dist = [[-1] * m for _ in range(n)]
    # 시작점 표시
    dist[sr][sc] = 0
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 범위 안이 아닌 경우
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            # 벽이거나 이미 방문한 곳인 경우
            if grid[nr][nc] == 1 or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    return dist

# 다중 시작점 BFS
def multi_bfs(grid, starts):
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    # 다중 시작점인 만큼 q에 다 넣어두고 시작
    for r, c in starts:
        dist[r][c] = 0
        q.append((r, c))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 범위 안이 아닌 경우
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            # 벽이거나 이미 방문한 곳인 경우
            if grid[nr][nc] == 1 or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))