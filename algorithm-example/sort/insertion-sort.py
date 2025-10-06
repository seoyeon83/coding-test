def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # key보다 큰 값을 오른쪽으로 이동
        # i부터 끝까지 j로 순회하면서 key보다 작은 값을 찾는다
        while j >= 0 and arr[j] > key:
            # print(i, j, key)
            # print(arr)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # print(arr)
    return arr 


print(insertion_sort([1,4,5,7,8,2,2,4,3]))