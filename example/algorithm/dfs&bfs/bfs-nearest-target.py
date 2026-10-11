# 가장 가까운 대상 찾기
# 거리 -> 행 -> 열 순서로 가장 우선인 대상 하나 고르기
# BFS는 거리 순서로 꺼내지니까, 최단 거리보다 먼 칸이 나오면 멈추기

from collections import deque

def nearest_target(grid, sr, sc, is_target, is_blocked):
    """is_target(r, c), is_blocked(r, c): 문제에 맞게 넘기는 함수.
    반환: (거리, r, c) 또는 None(갈 수 있는 대상 없음)"""

    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    best = None

    while q:
        r, c = q.popleft()
        # best가 이미 있고, 거리가 더 멀다면 중단
        if best is not None and dist[r][c] > best[0]:
            break
        # best 변경 (best가 없거나 key가 거리가 더 짧거나 좌표가 작은 경우)
        if (r, c) != (sr, sc) and is_target(r, c): # 시작 칸은 대상 X
            key = (dist[r][c], r, c)
            if best is None or key < best: 
                best = key
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if dist[nr][nc] != -1:
                continue
            if is_blocked(nr, nc):
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
    return best

