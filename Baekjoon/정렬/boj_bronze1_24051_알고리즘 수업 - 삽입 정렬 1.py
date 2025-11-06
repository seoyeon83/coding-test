'''
K 번재에 저장되는 수 구하기
pypy3으로 해야 ...
'''

import sys 


def insertion_sort(arr, N, K):
    cnt = 0

    for i in range(1, N):
        loc = i-1
        n = arr[i]

        while (0 <= loc and n < arr[loc]):
            arr[loc+1] = arr[loc]
            loc -= 1

            cnt += 1
            if cnt == K:
                return arr[loc+1]
        
        if loc + 1 != i:
            arr[loc+1] = n

            cnt += 1
            if cnt == K:
                return arr[loc+1]

    return -1


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(insertion_sort(A, N, K))