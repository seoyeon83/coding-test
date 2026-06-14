# 앞 뒤 번호에게만 빌릴 수 있다
# 여분을 가져온 학생이 도난 당했을 수도 있다

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 번호별 체육복 개수 체크
    case = [0] + [1] * n + [0]
    for l in lost:
        case[l] -= 1
    for r in reserve:
        case[r] += 1

    for l in lost:
        if case[l] == 0 : 
            if case[l - 1] > 1:
                case[l - 1] -= 1
                case[l] += 1

            elif case[l + 1] > 1:
                case[l + 1] -= 1
                case[l] += 1

    return n - case.count(0) + 2


'''
# 260614
접근: 배열에 학생별 체육복 개수를 저장해두고 순회하면서 계산. 그리고 가장 마지막에 answer 계산 (여벌을 가져온 체육복이 있는 학생이 도난당했을 수 있다)
개선:
    1) > 1, < 1대신 == 으로 명확하게 체육복 유무, 여벌 유무를 판단할 것
    2) 카운팅 루프 코드 간결화 (아니 이게 되네)
'''

def solution(n, lost, reserve):
    students = [0] + [1] * n + [0]

    for l in lost: students[l] -= 1
    for r in reserve: students[r] += 1
    
    for i in range(1, n+1):
        if students[i] < 1 and students[i-1] > 1:
            students[i-1] -= 1
            students[i] += 1
        elif students[i] < 1 and students[i+1] > 1:
            students[i+1] -= 1
            students[i] += 1
        
    answer = 0
    for s in students:
        if s > 0:
            answer += 1
            
    return answer

# 개선
def solution(n, lost, reserve):
    students = [0] + [1] * n + [0]

    for l in lost: students[l] -= 1
    for r in reserve: students[r] += 1
    
    for i in range(1, n+1):
        if students[i] == 0 and students[i-1] == 2:
            students[i-1] -= 1
            students[i] += 1
        elif students[i] == 0 and students[i+1] == 2:
            students[i+1] -= 1
            students[i] += 1
            
    return sum(s > 0 for s in students)