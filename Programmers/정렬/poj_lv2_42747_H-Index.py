# # len(citations) 부터 -1 하면서 h를 찾아야할듯
# def solution(citations):
#     answer = 0

#     for h in range(len(citations),0,-1):
#         if len(list(filter(lambda x: x>=h, citations))) >= h: return h
#     return 0

# 2025.10.06에 다시 푼 것
"""
이걸 count같은 걸로 리스트를 순회하지 않고 풀기 위해서는 정렬한 후 h번째 논문의 인용 횟수만 확인하면 되겠네?

6, 6, 5, 5, 0 이면 h=4가 되는 거네
리스트 중 가장 큰 값을 필두로 해서 해야겠네
그러니까 critations 최대값부터 1씩 빼가면서 순회하면 되겠네 

[5, 6, 7, 8] 처럼 n보다 그 논문들의 인용수가 큰 경우 h가 5로 나오는 경우를 방지하기 위해 리스트 정렬 후 0을 추가함
"""

def solution(citations):
    n = len(citations)+1
    citations.sort(reverse=True)
    citations.append(0)
    
    for h in range(citations[0], -1, -1):
        i = h-1 if (h-1) <= n-1 else n-1
        if citations[i] >= h:
            return h