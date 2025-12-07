'''
듣도 못한 사람의 명단, 보도 못한 사람의 명단
=> 듣도 보도 못한 사람의 명단

듣보잡의 수와 그 명단
set() 쓰면 되겠다
'''

import sys 

N, M = map(int, sys.stdin.readline().split())

a = set()
for _ in range(N):
    a.add(sys.stdin.readline().strip())

b = set()
for _ in range(M):
    b.add(sys.stdin.readline().strip())

result = sorted(a & b)
print(len(result))
for name in result:
    print(name)