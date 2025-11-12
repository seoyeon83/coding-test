from itertools import permutations


def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons):
        kk = k
        cnt = 0
        for d in p:
            if kk >= d[0]:
                kk -= d[1]
                cnt += 1
        
        if cnt > answer:
            answer = cnt
            
    return answer