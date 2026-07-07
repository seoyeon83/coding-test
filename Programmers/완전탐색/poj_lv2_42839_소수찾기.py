from itertools import permutations

def solution(numbers):
    # 에라토스테네스의 체로 소수 찾기
    n = int(''.join(sorted(numbers, reverse=True)))
    a = [False, False] + [True] * (n-1)
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
                
    # 순열로 만들 수 있는 조합을 찾고 소수인지 판별
    primes = set()
    for i in range(1, len(numbers)+1):
        for perm in permutations(list(numbers), i):
            c = int(''.join(perm ))
            if a[c]:
                primes.add(c)
    
    return len(primes)


print(solution("17"))

'''
# 260707
접근: 이 문제는 어떤 범위 내 소수 개수가 아니라 특정 숫자가 소수인지를 알아야 하므로 
에라토스테네스의 체는 비효율적이라고 생각해서 정석적인 방법으로 풀이함.
특히 신경 쓴 부분은 순열로 여러 경우의 수를 만들었을 때, numbers에 "0"이 포함되어 있다면
중복이 나올 수 있으므로 set()에 조합한 숫자들을 한 번에 저장한 뒤 순회함

개선점:
    - 소수 탐색 시 범위를 n//2까지 하기보다 로그 n으로 하는 게 더욱 효율적이다
    - 함수명 is_prime으로 직관적이게
    - if 조건문에서 not(n%i)보다 n%i == 0 으로 직관적이게
'''

from itertools import permutations

def func(n):
    if n <= 1: return False
    for j in range(2, n//2+1):
        if not(n%j):
            return False
    
    return True

def solution(numbers):
    s = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            s.add(int(''.join(p)))
        
    return sum(1 for n in s if func(n))

# 개선

from itertools import permutations

def is_prime(n):
    if n <= 1: return False
    for j in range(2, int(n**0.5) + 1):
        if n%j == 0:
            return False
    
    return True

def solution(numbers):
    s = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            s.add(int(''.join(p)))
        
    return sum(1 for n in s if func(n))