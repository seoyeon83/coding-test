### 집합을 활용해 푼 경우
# 상근이가 갖고 있는 숫자 카드 종류 (집합으로 중복 제거)
N = int(input())
n = set(map(int, input().split()))

# 정수 M개의 숫자 카드 
M = int(input())
m = list(map(int, input().split()))

# 정수 M 개의 숫자 카드 중, 상근이가 갖고 있는 경우 확인
for i in m :
    if i in n : print(1, end=' ')
    else : print(0, end=' ')

### 이분탐색 활용

# 상근이가 갖고 있는 숫자 카드 종류 (집합으로 중복 제거)
N = int(input())
n = sorted(map(int, input().split()))

# 정수 M개의 숫자 카드 
M = int(input())
m = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

for i in m :
    if binary_search(n, i) : print(1, end=' ')
    else : print(0, end=' ')