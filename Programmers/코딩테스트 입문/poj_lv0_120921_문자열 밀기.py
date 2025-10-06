'''
A를 밀어서 B가 될 수 있다면, 밀어야 하는 최소 횟수
A, B 길이: 1 ~ 99
완전탐색? 아예 찾지 못하면 -1 반환
'''
def solution(A, B):
    for i in range(100):
        if A == B:
            return i
        
        A = A[-1:] + A[:-1]
        
    return -1