'''
K번째 교환되는 수
배열 크기.. N이 매우 커서 시간 초과를 고민하고 있다...............

아니근데 애초에 선택정렬은 O(n^2)이잖아.. 
최적화를 해야하네.. 어떻게?
'''

import sys 

def selection_sort(arr, A, K):
    cnt = 0
    for i in range(A-1):
        last = A-1-i
        m = last
        # 범위 내 최댓값 구하기
        
        for j in range(A-i):
            if arr[j] > arr[m]:
                m = j

        if m != last:
            arr[m], arr[last] = arr[last], arr[m]
            cnt += 1
            if cnt == K:
                return print(arr[m], arr[last])
                

    if cnt < K:
        return print(-1)
        

A, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
selection_sort(arr, A, K)