'''
K 번 변경 직후 배열 A 출력
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
                for a in arr:
                    print(a, end=' ')
                return
        
        if loc + 1 != i:
            arr[loc+1] = n

            cnt += 1
            if cnt == K:
                for a in arr:
                    print(a, end=' ')
                return

    return print(-1)


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

insertion_sort(A, N, K)