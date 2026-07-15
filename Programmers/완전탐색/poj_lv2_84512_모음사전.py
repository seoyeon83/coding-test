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
'''