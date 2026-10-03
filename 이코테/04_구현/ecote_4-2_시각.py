'''
N 입력 -> 00시 00분 00초 ~ N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

00시 00분 3초
00시 13분 30초
'''

# 261003 처음 시도. 경우의 수를 계산해서 풀려고 했는데 그걸 제대로 계산 못해서 풀지 못한 케이스
import sys

N = int(sys.stdin.readline())

if N < 3:
    print(15*15*(N+1))
elif 3 <= N < 13:
    print(60*60 + 15*15*N)
elif 13 <= N < 22:
    print(60*60*2 + 15*15*(N-1))
else:
    print(60*60*3 + 15*15*(N-2))

# 위 코드를 개선한 버전
'''
0~59 중 3이 없는 수: 60 - 15 = 45개
분, 초 모두 3이 없는 경우: 45 * 45 = 2026
분, 초 중 하나라도 3이 있는 경우: 2600 - 2025 = 1575
'''
import sys

N = int(sys.stdin.readline())
h3 = sum(1 for h in range(N+1) if '3' in str(h))
# 시에 3이 든 경우는 60 * 60이므로 3600, 그리고 h3을 뺀 나머지 시간만큼 분, 초 중 3이 있는 경우를 곱해서 계산
print(h3 * 3600 + (N + 1 - h3) * 1575)


# 좀 더 정석적인 3중 반복문으로 푼 경우
import sys

N = int(sys.stdin.readline())

answer = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            # 3이 들어가 있는 건 어떻게 판단하지?
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                answer += 1

print(answer)