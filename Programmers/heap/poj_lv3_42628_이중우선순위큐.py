def solution(operations):
    q = list()
    
    for oper in operations:
        a, b = oper.split(' ')
        b = int(b)
        
        if a == 'I':
            q.append(b)
            q.sort()
        elif q:   
            if b > 0:
                q.pop()
            else:
                q.pop(0)
    
    return [max(q), min(q)] if q else [0, 0]