'''
K번 교환이 발생한 직후의 배열 A
시간 초과 고려

효율 좋은 알고리즘으로 

'''

import sys 


def selection_sort(arr, sorted_arr, N, K):
    location = {arr[i]:i for i in range(N)}
    cnt = 0

    for last in range(N-1, 0, -1):
        m = location[sorted_arr[last]]

        if last != m:
            arr[m], arr[last] = arr[last], arr[m]
            location[arr[last]], location[arr[m]] = last, m

            cnt += 1
            if cnt == K:
                for n in arr:
                    print(n, end=' ')
                return
    
    if cnt < K:
        return print(-1)


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

selection_sort(arr, sorted_arr, N, K)