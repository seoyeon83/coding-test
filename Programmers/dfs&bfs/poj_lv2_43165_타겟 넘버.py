

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


'''
260219
혼자서 풀기 성공! ㅎㅎ
'''

def solution(numbers, target):
    def dfs(n, i):
        if i == len(numbers):
            return 1 if n == target else 0
        
        return dfs(n + numbers[i], i+1) + \
            dfs(n - numbers[i], i+1)

    return dfs(0, 0)