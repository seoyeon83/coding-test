def bubble_sort(arr): 
    n = len(arr)
    # 한 번 돌면 마지막 값은 픽스
    for i in range(n):
        # i 값을 기준으로 j의 범위 설정
        # j 범위 안에서 앞뒤 값을 비교해서 그 범위 내 최대값이 가장 뒤로 가도록!!!
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr