import math


# 조합 / 순열 개수
print(math.sqrt(7))         # 7의 제곱근
print(math.sqrt(9))         # 9의 제곱근

import math

# 1. 정수 제곱근 (Python 3.8+)
print(math.sqrt(7))         # 7의 제곱근
print(math.sqrt(9))         # 9의 제곱근
print(math.isqrt(10))       # 3  (√10의 정수 부분)

# 2. 조합 / 순열 개수 (Python 3.8+)
print(math.comb(5, 2))      # 10 (5C2)
print(math.perm(5, 2))      # 20 (5P2)

# 3. 올림 / 내림
print(math.ceil(3.2))       # 4
print(math.floor(3.8))      # 3
# 반올림은 int(x + 0.5) 로 구현

# 4. 무한대 (최솟값/최댓값 초기화용) & pi와 자연상수 e
INF = math.inf              # float('inf')와 같음
print(math.pi)              # 파이(pi)
print(math.e)               # 자연상수 e

# 5. 곱 (Python 3.8+)
print(math.prod([1, 2, 3, 4]))  # 24 (1 * 2 * 3 * 4)

# 6. 두 점 사이 거리 (Python 3.8+)
print(math.dist((0, 0), (3, 4)))  # 5.0

# 7. 로그
print(math.log2(8))         # 3.0
print(math.log(100, 10))    # 2.0

# 8. 팩토리얼
print(math.factorial(5))    # 5! 5 팩토리얼

# 9. 최대공약수 & 최소공배수
print(math.gcd(21, 14))     # 최대공약수
print(math.lcm(21, 14))     # 최소공배수 (python 3.9부터 추가됨)