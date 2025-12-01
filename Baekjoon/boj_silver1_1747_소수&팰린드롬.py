'''
N보다 크거나 같고, 소수이면서 팰린드롬(뒤집어도 같은 수)인 수 중 가장 작은 수

소수 판별하는 데에 굉장한 시간이 걸릴듯..
에라토스테네스의 체를 이용해서 시간 단축
이때 문제는 탐색할 수의 범위의 끝이 정해지지 않았기 때문에 몇까지를 두고 탐색할지가 문제인데..
원래는 N * 10, N * 5로 했을 때도 통과가 됐음
그치만 실제로 N의 최대 범위인 1000000보다 크거나 같고, 소수이면서 팰린드롬인 수는 1000400 이내라서 범위를 그렇게 설정해두고 하니 상당히 빠르게 결과가 나옴!
'''

import sys


def check(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    return False


N = int(sys.stdin.readline())

n = 1004000 # 범위
a = [False,False] + [True]*(n-1) # 체, 확실히 소수가 아닐 경우 False
primes=[]

for i in range(2,n+1):
    if a[i]: # i는 소수인가?
        if i >= N and check(i):
            print(i)
            break
        
        primes.append(i) # i를 소수로 채택 후, i의 배수를 지운다
        for j in range(2*i, n+1, i):
            a[j] = False