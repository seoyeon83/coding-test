'''
정렬 과정에서 배열 A, B가 같은 경우가 발생하는지 확인
'''

import sys 

def equals(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
        
    return True


def insertion_sort(arr, target, N):
    for i in range(1, N):
        loc = i-1
        n = arr[i]

        while (0 <= loc and n < arr[loc]):
            arr[loc+1] = arr[loc]
            loc -= 1

            if equals(arr, target):
                return 1
        
        if loc + 1 != i:
            arr[loc+1] = n

            if equals(arr, target):
                return 1

    return 0


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

if equals(A, B):
    print(1)
else:
    print(insertion_sort(A, B, N))