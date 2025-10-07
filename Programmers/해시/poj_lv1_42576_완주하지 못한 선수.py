'''
마라톤 참여 선수 participant, 완주 선수 completion
완주하지 못한 선수 이름 return 
동명이인이 있음
완주하지 못한 선수는 1명

두 배열을 정렬 후 비교?
비교하다가 두 값이 같지 않은 경우가 생기면 그 participant 값이 미완주자
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]
    