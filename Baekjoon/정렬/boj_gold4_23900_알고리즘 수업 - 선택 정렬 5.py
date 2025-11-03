'''
N 시간 초과 고려
오름 차순 정렬 중 A와 B가 같은 경우가 발생하는가
초기 상태 배열 A도 B가 될 수 있다
같은 경우 발생 -> 1, 아니면 0

빠르게 하는 경우는 다른 빠른 알고리즘으로 정렬된 sorted_arr을 이용하는 것
현재 배열, arr의 위치를 빠르게 검색할 수 있도록 딕셔너리에 저장해둔다

시간이 많이 드는 최댓값을 찾는 과정을 
'''

import sys

def selection_sort(arr, sorted_arr, target, N):
    location = {arr[i]: i for i in range(N)}

    for last in range(N-1, 0, -1):
        # 범위 중 최댓값의 위치
        m = location[sorted_arr[last]]

        # 교환
        if m != last:
            arr[m], arr[last] = arr[last], arr[m]
            location[arr[m]], location[arr[last]] = m, last
            if equals(arr, target):
                return 1

    return 0


def equals(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

sorted_A = sorted(A)

if equals(A, B):
    print(1)
else:
    print(selection_sort(A, sorted_A, B, N))