# len(citations) 부터 -1 하면서 h를 찾아야할듯
def solution(citations):
    answer = 0

    for h in range(len(citations),0,-1):
        if len(list(filter(lambda x: x>=h, citations))) >= h: return h
    return 0