'''
0 ~ 99
(주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고), 각 자리의 숫자를 더한다
주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙인다

- 6 => 0 + 6 = 6 
- 26 => 2 + 6 = 8 => 68
- 6 + 8 = 14 => 84
- 8 + 4 = 12 => 42
- 4 + 2 = 6 => 26
26의 사이클은 4

N의 사이클의 길이, 즉 다시 자신이 되려면 얼마나 걸리나?
'''

import sys 

N = sys.stdin.readline().strip()
target = N
answer = 0

while N != target or answer < 1:
    answer += 1

    if len(N) > 1:
        N = str((int(N[0]) + int(N[1]))%10 + int(N[1])*10)
    else:
        N = str(int(N[0]) + int(N[0])*10)

print(answer)