def solution(nums):
    n = len(nums)//2
    x = len(set(nums))
    return x if n>x else n