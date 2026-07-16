def solution(word):
    
    weight = [781, 156, 31, 6, 1]
    index = {"A":0, "E":1, "I":2, "O":3, "U":4}
    
    answer = 0
    for i, c in enumerate(word):
        answer += (weight[i] * index[c]) + 1
    
    return answer


print(solution("AAAAE"))


'''
# 260715 
다시 봐도 어떻게 푸는지 모르겠어서 지난 풀이를 보고 다시 따로 정리해봤다

# 260716
어제 풀었을 때 익힌 것을 기반으로 혼자 풀어봤다. 이제 이 풀이과정을 제대로 기록해둬야지
'''
def solution(word):
    idx = {"A":0, "E":1, "I":2, "O":3, "U":4}
    weight = [781, 156, 31, 6, 1]
    
    answer = 0
    for i, c in enumerate(word):
        answer += weight[i] * idx[c] + 1
    return answer