'''
다른 분께서 풀이하신 코드 (O(N))
stack은 가격이 끝까지 떨어지지 않는 시간의 인덱스를 저장
가격이 떨어지는 순간은 while문에 걸려 결과로 기록됨
마지막 반복문으로 리스트의 길이와 인덱스 값으로 얼마동안 가격이 떨어지지 않는지 기록 
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
    
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    for i in stack:
        answer[i] = len(prices) - 1 - i

    return answer


'''
260129
전에 푼 것보다 보기 편한 것 같음
근데 이것도 다른 분 풀이를 훑어보고 내가 짠 거라.. 다음에 다시 풀어봐야한다
'''

from collections import deque

def solution(prices):
    answer = list()
    queue = deque(prices)
    
    while queue:
        n = queue.popleft()
        cnt = 0
        
        for price in queue:
            cnt += 1
            if n > price:
                break
        
        answer.append(cnt)
    
    return answer