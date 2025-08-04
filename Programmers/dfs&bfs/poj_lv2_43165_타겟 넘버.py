

def dfs(numbers, target, index, summary):
    if index == len(numbers):
        if summary == target:
            return 1
        return 0
    
    p = dfs(numbers, target, index+1, summary+numbers[index])
    m = dfs(numbers, target, index+1, summary-numbers[index])

    return p + m
        
    
def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

print(solution([4, 1, 2, 1], 4))