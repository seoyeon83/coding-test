'''
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
S가 최솟값이 되도록 A를 재배열, B는 그대로 
S의 최솟값을 출력

가장 이상적인 방법은 B의 큰 수에 A의 작은 수를 매칭하는 것
A, B 모두 정렬 후 서로 곱해서 더하면 되는 거 아닌가
'''
import sys

N = int(sys.stdin.readline())
A = sorted(map(int, sys.stdin.readline().split()))
B = sorted(map(int, sys.stdin.readline().split()), reverse=True)

ans = sum(A[i]*B[i] for i in range(N))

print(ans)

