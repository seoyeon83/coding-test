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
                    for a in arr:
                        print(a, end=" ")
                    return 0

    if cnt < K:
        return print(-1)

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

bubble_sort(A, N, K)