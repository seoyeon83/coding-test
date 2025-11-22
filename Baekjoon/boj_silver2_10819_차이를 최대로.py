'''
이웃한 수의 차이의 합을 구할 때 최댓값이 나오도록
흠
가장 큰 수 - 가장 작은 수 + 가장 작은 수 - 두 번째로 큰 수 + ...
이렇게 해야 가장 차이가 크지 않을까 


근데 만약 주어진 배열의 길이가 홀수라면? 그 중간에 있는 수는 배제?
일단 수식이 주어진 것이 있으니 그렇다고 가정하자

아니근데 정렬로 해결되는 건 아닌듯..

모든 경우의 수로 거의 완전탐색처럼 해봐야할 것 같은데

완전 탐색.. 순열? N의 범위는 좁으므로..


'''

import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
new_nums = list()

answer = 0
for perm in permutations(nums):
    temp = 0
    for i in range(N-1):
        temp += abs(perm[i] - perm[i+1])
    if temp > answer:
        answer = temp

print(answer)