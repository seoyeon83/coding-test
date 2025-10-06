def selection_sort(arr):
    # 가장 작은 값을 맨 앞과 교환한다
    for i in range(len(arr)-1):
        # 가장 작은 값을 찾아
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j 

        arr[i], arr[m] = arr[m], arr[i]
    
    return arr


print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]