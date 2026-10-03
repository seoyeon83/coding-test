'''
itertools.permutations: 순열 (같은 원소 중복 X)
itertools.combinations: 조합 (같은 원소 중복 X)
itertools.product: 순열인데 중복 허용
itertools.combinations_with_replacement: 조합인데 중복 허용
'''

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

print(list(permutations(data, 3)))
print(list(combinations(data, 3)))
print(list(combinations(data, 2)))
print(list(product(data, repeat=3)))
print(list(combinations_with_replacement(data, 2)))