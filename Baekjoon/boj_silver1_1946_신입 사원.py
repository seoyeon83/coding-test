'''
서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
즉, 다른 모든 사람들보다 서류, 면접 둘 중 하나의 점수는 높아야 한다는 것
신입사원의 최대 인원수 

그냥 단순화게 비교? => 시간 초과가 됨

오름차숱 정렬 후 나보다 순위가 높은 애들만 비교?
'''

# import sys 

# def check(i, score):
#     for j in range(0, i):
#         if score[i][1] > score[j][1]:
#             return False
    
#     return True

# for _ in range(int(sys.stdin.readline())):
#     N = int(sys.stdin.readline())
#     score = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
#     score.sort(key=lambda x: x[0])

#     answer = 1
#     for i in range(1, N):
#         if check(i, score):
#             answer += 1

#     print(answer)

import sys 


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    score = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    score.sort(key=lambda x: x[0])

    answer = 1
    # 가장 좋은 면접 성적을 저장해두기
    # i가 이 면접 성적보다 좋으면 answer += 1, min_rank 갱신
    min_rank = score[0][1]
    for i in range(1, N):
        if min_rank > score[i][1]:
            answer += 1
            min_rank = score[i][1]

    print(answer)