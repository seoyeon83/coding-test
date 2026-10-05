# 2차원 리스트(격자) 복사
def copy_grid(grid):
    return [row[:] for row in grid]

# 시계방향 90도 회전 (n * m -> m * n, clockwise)
# 회전된 방향대로 출력만 해주면 된다
# r, c = c, r
# c번째 열을 아래(n-1)부터 위로 읽는다
def rotate_cw(grid):
    n, m = len(grid), len(grid[0])
    return [[grid[n - 1 - r][c] for r in range(n)] for c in range(m)]

# 한 줄 버전 (행을 뒤집고 전치(zip(*grid), 전치는 행과 열 바꾸는 것)
cw  = [list(row) for row in zip(*grid[::-1])]

# 반시계방향 90도 회전 (counter-clockwise)
# 마지막 열부터(m-1-c) 위에서 아래(r)로 읽는다
def rotate_ccw(grid):
    n, m = len(grid), len(grid[0])
    return [[grid[r][m - 1 - c] for r in range(n)] for c in range(m)]

# 한 줄 버전 (전치(행과 열 바꾸기)하고 행을 뒤집기
ccw = [list(row) for row in zip(*grid)][::-1]

# 부분 정사각형 시계 회전 ((sr, sc)에서 시작하는 size * size 구역만 회전)
def rotate_sub_cw(grid, sr, sc, size):
    # 그 부분만 잘라내기 (구역의 각 줄을 돌면서 필요한 열만 잘라내기)
    sub = [grid[sr + i][sc:sc + size] for i in range(size)]
    # 그 부분만 돌리기
    rotated = rotate_cw(sub)
    # 다시 붙이기 (구역의 각 칸을 돌면서 값 대입하기)
    for i in range(size):
        for j in range(size):
            grid[sr + i][sc + j] = rotated[i][j]