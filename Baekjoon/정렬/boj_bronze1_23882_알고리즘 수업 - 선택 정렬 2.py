'''
K번 교환 발생 직후 배열 A 출력
교환 횟수가 K보다 작으면 -1 출력

큰 수 찾아서 맨 뒤랑 교환 
'''

import sys 

def selection_sort(arr, A, K):
    cnt = 0
    for i in range(A-1):
        last = A-i-1
        m = last 
        # 범위 대 최대 찾기
        for j in range(last):
            if arr[j] > arr[m]:
                m = j

        if m != last:
            arr[m], arr[last] = arr[last], arr[m]
            cnt += 1
            if cnt == K:
                for x in arr:
                    print(x, end=' ')
                return
    
    if cnt < K:
        print(-1)
        return

A, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

selection_sort(arr, A, K)