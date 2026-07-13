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


'''
# 260713
접근: 순열로 모든 경우를 구해서 탐색한다
개선: 변수명, 생략 가능한 부분

안그래도 풀 때 dfs로도 가능하겠다 싶었는데.. 다음에는 dfs로 해보면 좋겠다
'''

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons, len(dungeons)):
        cnt, kk = 0, k
        
        for a, b in per:
            if kk >= a: 
                kk -= b
                cnt += 1
            else: break
            
        if cnt > answer:
            answer = cnt
        
    return answer

# 개선

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons):
        cnt, cur_k = 0, k
        
        for need, cost in per:
            if cur_k >= need: 
                cur_k -= cost
                cnt += 1
            else: break
            
        answer = max(cnt, answer)
        
    return answer