'''
파이프에서 물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리

길이가 L인 테이프를 무한개 갖고 있다
그 위치의 좌우 0.5만큼의 간격을 줘야 다시는 물이 안 샌다
필요한 테이프의 최소 개수
테이프는 자를 수 없고, 겹쳐서 붙일 수 있다 


물이 새는 곳 개수 N, 테이프 길이 L
물이 새는 곳의 위치

여러 위치의 거리가 가까우면 테이프 하나로도 막을 수 있겠네

테이프가 끝나는 지점을 저장해둔다
'''

import sys 


N, L = map(int, sys.stdin.readline().split())
spots = sorted(map(int, sys.stdin.readline().strip().split()))

answer = 0
tape = -1

# 테이프가 붙여지는 범위 안이면 넘어가고
# 테이프가 붙여진 범위를 넘어갔다면 테이프 추가
for spot in spots:
    if tape < spot:
        tape = spot + L - 0.5
        answer += 1

print(answer)