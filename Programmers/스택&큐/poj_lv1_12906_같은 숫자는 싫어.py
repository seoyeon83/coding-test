def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for n in arr:
        if answer[-1] != n:
            answer.append(n)
            
    return answer


# 260609 2번째 풀이
def solution(arr):
    answer = arr[:1]
    for a in arr[1:]:
        if a == answer[-1]:
            continue
        answer.append(a)
        
    return answer

# 260609 2번째 풀이 (개선)
def solution(arr):
    answer = arr[:1]
    for a in arr[1:]:
        if a != answer[-1]:
            answer.append(a)
            
    return answer