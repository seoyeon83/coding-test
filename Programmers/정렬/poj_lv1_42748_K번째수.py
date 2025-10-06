def solution(array, commands):
    return [sorted(array[arr[0]-1:arr[1]])[arr[2]-1] for arr in commands]
    
    
# 풀어 쓴 버전
def solution(array, commands):
    answer = []
    for arr in commands:
        sorted_arr = sorted(array[arr[0]-1:arr[1]])
        answer.append(sorted_arr[arr[2]-1])
    
    return answer

# 2025.10.06에 다시 푼 버전 (가독성 좋게)

# i ~ j 번째 숫자까지 자르고 정렬했을 때, k 번째에 있는 수?
# 자른 그 범위 안에서 

def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    
    return answer