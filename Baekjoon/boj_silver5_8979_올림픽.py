import sys 

# a가 b보다 순위가 높으면 T, 아니면 F
def f(a, b):
    if (a[0] > b[0]) \
    or (a[0] == b[0] and a[1] > b[1]) \
    or (a[0] == b[0] and a[1] == b[1] and a[2] > b[2]):
        return True
    return False


N, K = map(int, sys.stdin.readline().split())

medals = dict()
for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    medals[i[0]] = i[1:]

# K보다 순위가 높은 국가 개수 카운트
cnt = 1 + sum(f(medals[n], medals[K]) for n in range(1, N+1) if K != n)

print(cnt)