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