'''
100, 90, 90, 80 => 1, 2, 2, 4등
태수의 새 점수가 랭킹 리스트에서 몇 등인가?
랭킹 안에 들어간다면 자기 점수보다 높은 점수의 개수 + 1

랭킹리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다 

N: 랭킹 개수
P: 랭킹리스트 공간
'''

import sys 

N, new_record, P = map(int, sys.stdin.readline().split())

if N == 0:
    print(1)
else:
    rank = list(map(int, sys.stdin.readline().split()))

    if N == P and rank[-1] >= new_record:
        print(-1)

    else:
        answer = 1
        for i in rank:
            if i > new_record:
                answer += 1
            else:
                break

        print(answer)