def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    print(left, right)
    # 두 배열을 비교해 병합
    # left, right 중 하나라도 배열을 다 순회하면 끝난다
    # 어차피 left, right도 merge를 통해 온 것이기 때문에 left, right 각각 안은 정렬이 되어있는 상태
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1 
        print("result", result)
        print("i", i, "j", j)
    
    # 남은 원소 추가 (남은 원소가 생기나?)
    print("남은 원소", left[i:], right[j:])
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(merge_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]