def solution(n, times):
    answer = 0
    left, right = 1, min(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        total_people = sum(mid // t for t in times)
        
        if total_people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer