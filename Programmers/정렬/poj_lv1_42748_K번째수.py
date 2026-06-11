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

'''
# 260611

접근: 1-index(input)을 0-index로 변환하고 파이썬의 리스트 슬라이싱을 활용
개선:
    1) 리스트 초기화 시 list() 말고 []를 활용할 것.
        왜? []는 리터럴 문법이라서 인터프리터가 빈 리스트를 바이트코드 하나로 처리 가능. list()는 함수 호출이라서 단계가 더 많아진다 (느려지겠죠)
        list()는 이터러블을 리스트로 변환할 때. list("abc"), list(range(5)), list({1, 2, 3})
    2) 컴프리헨션 적용 가능 => [sorted(array[start-1:end])[target-1] for start, end, target in commands]
        변환 로직이 단순하고 한 눈에 읽힐 때는 적용하는 게 좋음
        이걸 쓰면 코드가 짧아지므로 너무 복잡하지만 않으면 연습해서 실전에서 사용할 가치가 있음
'''
def solution(array, commands):
    answer = list()
    for start, end, target in commands:
        arr = sorted(array[start-1:end])
        answer.append(arr[target-1])
        
    return answer

def solution(array, commands):
    return [sorted(array[start-1:end])[target-1] for start, end, target in commands]