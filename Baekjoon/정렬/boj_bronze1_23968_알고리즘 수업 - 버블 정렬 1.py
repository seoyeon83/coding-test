'''
오름차순하고 k번째 교환되는 수 
버블정렬은 한 텀에 앞뒤 값을 비교해서 앞 수가 더 크면 위치를 바꾸는 알고리즘
O(n^2)

Python3은 인터프리터 언어 특성때문에 시간초과가 불가피함
그래서 Pypy3으로..
'''

import sys 

def bubble_sort(arr, N, K):
    cnt = 0
    for last in range(N-1, 0, -1):
        for i in range(last):
            # 교환 
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                cnt += 1
                if cnt == K:
                    return print(arr[i], arr[i+1])

    if cnt < K:
        return print(-1)

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

bubble_sort(A, N, K)