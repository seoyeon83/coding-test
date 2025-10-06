# 최소힙으로 내림차순 정렬 구현하기

def heapify(arr, n, i): # 배열, 배열 길이, 기준점(루트)
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left 
    if right < n and arr[right] < arr[smallest]:
        smallest = right 
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    print(arr)

    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)
        print(arr, j)
    
    return arr

print(heap_sort([11, 12, 22, 25, 64]))