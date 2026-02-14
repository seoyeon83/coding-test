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



'''
260215
'''

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for perm in permutations(dungeons):
        cur_k = k
        cnt = 0
        
        for a, b in perm:
            if a <= cur_k:
                cur_k -= b
                cnt += 1
            
        if cnt > answer:
            answer = cnt
            
    return answer