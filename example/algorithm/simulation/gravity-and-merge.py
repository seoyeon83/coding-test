# 중력: 0이 아닌 값을 각 열의 아래로 떨어뜨리기 (2048, 뿌요뿌요류)
def gravity(grid):
    n, m = len(grid), len(grid[0])
    # 열을 기준으로 순회하면서 각 칸의 값이 0이 아닌 칸을 stack에  [2, 0, 3, 0]
    for c in range(m):
        stack = [grid[r][c] for r in range(n) if grid[r][c] != 0]
        # 0이 아닌 값을 아래부터 채운다 -> [0, 0, 2, 3]
        for r in range(n - 1, -1, -1):
            grid[r][c] = stack.pop() if stack else 0


# 2048 한 줄 합치기 (왼쪽 밀기)
'''
예:
  [2, 2, 2, 0] → [4, 2, 0, 0]   (앞의 두 개만 합쳐짐)
  [2, 2, 4, 0] → [4, 4, 0, 0]   (합쳐진 4가 또 합쳐지지 않음)
  [4, 4, 4, 4] → [8, 8, 0, 0]

1. 0을 빼고 숫자만 모은 뒤
2. 앞에서부터 같은 수가 붙어 있으면 합치고 두 칸을 건너뛴다 (i += 2) 
    -> 그래서 한 번 합쳐진 건 다시 합쳐지지 않는 것
3. 남은 자리는 0으로 채운다
'''

def merge_left(line):
    nums = [x for x in line if x != 0]
    out, i = [], 0
    while i < len(nums):
        # 다음 인덱스와 수가 같은 경우 합치고 이동
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            out.append(nums[i] * 2)
            i += 2
        # 같지 않으면 다음 인덱스로 이동
        else:
            out.append(nums[i])
            i += 1
    # 남은 자리 0으로 채우고 return
    return out + [0] * (len(line) - len(out))