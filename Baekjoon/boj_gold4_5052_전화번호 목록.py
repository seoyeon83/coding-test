'''
긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26
선영에게 전화를 걸 수 없음 => 일관성 X

즉, A의 번호가 B 번호의 접두어라면 일관성이 없는 것
근데 하나씩 비교하는 방법이 있긴 하지만... O(n^2)이 나와서 시간초과가 될 것 같은데
일단 비교할 때, 자신 전화번호의 길이보다 짧아야 함. 중복이 없어야 하니까

pypy3 으로 하면 맞긴 한데./... python3으로 하면 시간 초과

글자수와 오름차순 정렬 후에 진행
반복문 돌릴 때 글자수 기반으로 슬라이싱이 가능하면 좋을텐데
2차원 배열로 만들까? -> 좀 더 시간 개선이 되긴 했다
'''

## PyPy3: 4832ms, 113740KB
# import sys 

# def func(nums):
#     for i in nums:
#         for j in nums:
#             if len(j) > len(i) and i == j[:len(i)]:
#                 return "NO"

#     return "YES"

# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     nums = [sys.stdin.readline().strip() for _ in range(n)]

#     print(func(nums))


## PyPy3: 1304ms, 115560KB
import sys 

def func(numslen):
    for i in range(1, 11):
        for num in numslen[i]:
            for j in range(1, i):
                for num2 in numslen[j]:
                    if num[:j] == num2:
                        return "NO"

    return "YES"

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    nums = [sys.stdin.readline().strip() for _ in range(n)]
    numslen = [[] for _ in range(11)]
    for num in nums:
        numslen[len(num)].append(num)

    print(func(numslen))

