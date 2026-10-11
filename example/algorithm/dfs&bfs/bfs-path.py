# BFS 경로 복원
# 최단 거리 뿐만 아니라 어떤 칸들을 지나가는지가 필요할 때
# prev에 이전 칸을 기록해 두고 도착점부터 거꾸로 따라간다
# 같은 길이의 경로가 여럿이면 dr, dc의 탐색 순서가 어떤 경로를 고를지 정한다
# 문제의 방향 우선순위에 맞게 dr, dc 순서 맞출 것
from collections import deque

def bfs_path(grid, sr, sc, er, ec, is_blocked):
    ''' 반환: 시작 칸부터 도착 칸까지의 칸 목록, 갈 수 없으면 None '''
    n, m = len(grid), len(grid[0])
    prev = [[None] * m for _ in range(n)]
    prev[sr][sc] = (sr, sc)
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        if (r, c) == (er, ec):  # 도착지
            break
        for d in range(4):      # 우선하는 방향 순으로 순회
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if prev[nr][nc] is not None:    # 이건 왜 막지? 이미 방문해서?
                continue
            if is_blocked(nr, nc):
                continue
            prev[nr][nc] = (r, c)
            q.append((nr, nc))

    if prev[er][ec] is None:    # 도달 못함 (경로 존재 안함)
        return None

    # path에 끝점부터 리스트에 삽입
    path = []
    r, c = er, ec
    while (r, c) != (sr, sc):
        path.append((r, c))
        r, c = prev[r][c]
    path.append((sr, sc))
    path.reverse()  # 시작점이 맨 처음에 오도록 변환
    return path
