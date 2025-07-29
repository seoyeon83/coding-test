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