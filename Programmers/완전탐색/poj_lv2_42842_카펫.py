def solution(brown, yellow):
    
    n = brown+yellow # 넓이
    h = 3 # 최소 높이
    while True:
        w = n//h
        # 넓이가 h로 나누어 떨어지는지, 제대로 그 카펫이 맞는지 확인 
        if n%h==0 and (w+h-2)*2==brown:
            return [w, h]
        h += 1

print(solution(10, 2))