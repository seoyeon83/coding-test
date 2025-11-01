'''
배열 A를 선택정렬로 오름차순 정렬하는 과정 중 A와 B가 같은 경우가 발생하면 1, 아니면 0
단순히 매번 모든 원소를 비교할 수도 있긴 한데 좀 효율적인 방법이 없는가 
'''

import sys

def equals(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return False    
    return True


def selection_sort(N, A, B):
    for last in range(N-1, 0, -1):
        m = last

        # 최댓값 찾기 
        for i in range(last):
            if A[i] > A[m]:
                m = i
        
        # 교환하기
        if m != last:
            A[m], A[last] = A[last], A[m]
            if equals(A, B):
                return 1
    
    return 0


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

if equals(A, B):
    print(1)
else:
    print(selection_sort(N, A, B))