# k개의 랜선을 같은 길이를 가진 n개의 랜선으로 만들 때, 만들 수 있는 최대 랜선의 길이
# 항상 cm 단위로 정수 길이만큼 자른다
# n 개 이상 만들 수도 있다
# 이때 만들 수 있는 최대 랜선의 길이 

# k, n (k<=n)
k, n = map(int, input().split(' '))
# k개의 랜선의 각 길이
lengths = [int(input()) for _ in range(k)]

# n 개로 만들 수 있는 랜선의 최소, 최대(주어진 랜선 중 최대값) 길이
low, high = 1, max(lengths)
result = 0

while low <= high:
    # 랜선 길이의 중간 값
    mid = (low + high) // 2
    # mid로 k개의 랜선을 잘랐을 때 나올 수 있는 랜선의 개수
    cnt = sum(length // mid for length in lengths)
    
    # 그 랜선의 개수가 n 개 이상인가?
    if cnt >= n:
        result = mid  # 조건을 만족하므로 결과값 업데이트
        low = mid + 1  # 더 큰 길이를 탐색
    else:
        high = mid - 1  # 더 작은 길이를 탐색

print(result)