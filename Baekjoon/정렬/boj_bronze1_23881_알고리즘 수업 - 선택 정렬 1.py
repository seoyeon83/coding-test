'''
선택 정렬: 한바퀴돌때가장작은값을찾아맨앞과교환하는방식
-> 맨 앞에 작은 값이 쌓이게 된다 
A를 오름차순 정렬할 경우, K번재 교환되는 수를 찾기

범위 중에서 가장 큰 
'''
import sys


def selection_sort(arr, K):
    cnt = 0
    for i in range(len(arr)):
        last = len(arr)-1-i
        m = last
        # 범위 내 최댓값 구하기
        
        for j in range(len(arr)-i):
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
selection_sort(arr, K)