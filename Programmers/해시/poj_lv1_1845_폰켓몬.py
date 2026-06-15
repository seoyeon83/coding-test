def solution(nums):
    n = len(nums)//2
    x = len(set(nums))
    return x if n>x else n

'''
260615
접근: 최대로 가져갈 수 있는 종류의 개수를 원하기 때문에 
    종류의 개수를 세서 n/2보다 적으면 그 종류의 개수를 반환하고, 그게 아니면 n/2 반환
개선: 조건문 말고 min() 사용하기

'''

def solution(nums):
    uniq = len(set(nums))
    n2 = len(nums)//2
    return n2 if uniq >= n2 else uniq

# 개선
def solution(nums):
    uniq = len(set(nums))
    n2 = len(nums)//2
    return min(uniq, n2)