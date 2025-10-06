def solution(quiz):
    answer = []
    
    for q in quiz:
        q = q.split(' ')
        
        res, ans = int(q[0]), int(q[-1])
        for i in range(1, len(q)//2, 2):
            if q[i] == "+": res += int(q[i+1])
            elif q[i] == "-": res -= int(q[i+1])
        
        if res == ans: answer.append("O")
        else: answer.append("X")
        
    return answer