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
    
'''
# 260610 재시도

접근: kv 형태로 이름별 참가자 수를 세고, 이후 완주자 이름으로 숫자를 차감. 그 뒤에도 0 초과인 경우를 찾아 반환 (해시맵으로 count 관리)
복잡도: O(n)
개선: 
    c[name] = c[name] + 1 if c.get(name, 0) else 1 
    -> c[name] = c.get(name, 0) + 1 으로 로직 개선

    c라고 간단히 정의한 변수명을 더 명확하게 하면 좋을듯
    -> 혹은 collections.Counter를 사용하는 것도 방법! (와 이게된다고?)
    
    ```
    from collections import Counter
    
    def solution(participant, completion):
        diff = Counter(participant) - Counter(completion)
        return next(iter(diff))
    ```
'''
def solution(participant, completion):
    c = dict()
    for name in participant:
        c[name] = c.get(name, 0) + 1
    
    for name in completion:
        c[name] -= 1
    
    for k, v in c.items():
        if v > 0:
            return k