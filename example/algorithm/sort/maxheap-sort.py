# 재귀적으로 최대힙 만들기
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # left, right 중 largest보다 더 큰 값이 있으면 위치 바꾸기
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 최대힙 만들기
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    print(arr)

    # 정렬
    # 맨 뒤부터 앞뒤 값을 바꾸고 다시 최대힙 구조로 만든다
    # 맨 앞, 즉 인덱스 0을 최대힙으로 만들고, i과 계속 이걸 바꾸면서 뒤쪽에 큰 값들이 쌓이는 구조!!!
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr 


print(heap_sort([11, 12, 22, 25, 64]))  
# [11, 12, 22, 25, 64]
# [64, 25, 12, 22, 11]