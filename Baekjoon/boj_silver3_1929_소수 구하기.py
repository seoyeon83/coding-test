'''
M 이상, N 이하의 소수 모두 구하기
'''
import sys 

M, N = map(int, sys.stdin.readline().split())
n = N
a = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        if M <= i:
            primes.append(i)

        for j in range(2*i, n+1, i):
            a[j] = False

for p in primes:
    print(p)


### 에라토스테네스의 체 사용 X -> 시간 초과

# import sys 


# def isPrime(n):
#     for i in range(2, n//2+1):
#         if n%i==0:
#             return False
#     return True


# M, N = map(int, sys.stdin.readline().split())
# primes = []

# for i in range(M, N+1):
#     if isPrime(i):
#         primes.append(i)

# for p in primes:
#     print(p)