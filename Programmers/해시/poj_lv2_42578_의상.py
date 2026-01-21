'''
얼굴, 상의, 하의, 겉옷 중 매일 다른 옷을 조합한다
각 종류별로 최대 1가지 의상만 착용할 수 있다
착용한 의상의 일부가 겹쳐도.. 다른 의상이 겹치지 않거나 추가로 더 착용한 경우 다른 방법으로 본다
즉, 조합이 달라야한다는 거 아닌가?
최소 하루에 한 개의 이상은 입는다

서로 다른 옷의 조합의 수를 return 
각 종류를 카운트하고 경우의 수 계산

[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
headgear: 2, eyewear:1
2 + 1 + 2*1


종류별로 그거 하나만 입는 경우
3 * 2 - 1 (0개 입는 경우 빼기)
'''

def solution(clothes):
    # 종류별 의상 수 카운트 
    cnt = dict()
    for _, c in clothes:
        if c in cnt.keys():
            cnt[c] += 1
        else:
            cnt[c] = 2

    answer = 1
    for k, v in cnt.items():
        answer *= v
        
    return answer - 1


'''
260121 다시 풀이함
어떻게 이렇게 똑같이 풀었을까..
차이점: dict에 key 값 유무를 판단하는 방식.. 인데 category in d가 더 권장된다네
앞으로는 그렇게 하는 것으로!
'''
def solution(clothes):
    # dict로 각 의상별 개수 기록
    d = dict()
    for _, category in clothes:
        if category in d:
            d[category] += 1
        else:
            d[category] = 2
    
    # 경우의 수 계산
    answer = 1
    for _, v in d.items():
        answer *= v
    
    # 아예 안 입은 하나의 경우를 제외
    return answer - 1