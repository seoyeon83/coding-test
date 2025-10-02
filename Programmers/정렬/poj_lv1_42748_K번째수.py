def solution(array, commands):
    return [sorted(array[arr[0]-1:arr[1]])[arr[2]-1] for arr in commands]
    
    
# 풀어 쓴 버전
def solution(array, commands):
    answer = []
    for arr in commands:
        sorted_arr = sorted(array[arr[0]-1:arr[1]])
        answer.append(sorted_arr[arr[2]-1])
    
    return answer