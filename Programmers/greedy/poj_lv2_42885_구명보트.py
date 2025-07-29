def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # 내림차순 정렬
    
    # 리스트의 첫, 마지막 인덱스로 초기화. l과 r이 같거나(1명만 남은 경우) 큰 경우 반복
    l, r = 0, len(people)-1 
    while l <= r:
        answer += 1
        
        if l == r:  # 1명만 남은 경우 -> 구조 후 break
            break

        # people 내 최소, 최대 몸무게 합이 limit을 넘지 않을 경우 둘 모두 구조
        if people[l] + people[r] <= limit:
            r -= 1
        
        # 최소, 최대 몸무게의 합이 limit을 넘을 경우 몸무게가 최대인 1인만 구조
        l += 1
            
    return answer