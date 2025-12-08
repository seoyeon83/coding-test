'''
아홉 난쟁이의 키가 주어졌을 때, 키의 합이 100이 되는 경우 일곱 난쟁이의 키를 오름차순으로 출력
순열 함수 쓰면 되지 않을까
'''

from itertools import combinations
import sys

a = [int(sys.stdin.readline()) for _ in range(9)]

for perm in combinations(a, 7):
    if sum(perm) == 100:
        for p in sorted(perm):
            print(p)
        sys.exit(0)