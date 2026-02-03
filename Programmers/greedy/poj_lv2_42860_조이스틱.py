def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for i, c in enumerate(name):
        # 알파벳 이동
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
        
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        min_move = min(min_move, 2 * i + n - next_idx, i + 2 * (n - next_idx))
        
    answer += min_move
        
    return answer