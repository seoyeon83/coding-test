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

'''
# 260625
접근: 스택에 아직 가격이 떨어지지 않은 인덱스를 저장한다

이번에도 도무지 모르겠어서 클로드한테 힌트를 좀 받아서 풀었다
이전에는 큐로 풀었는데 이번에는 스택으로! 근데 스택이 더욱 문제가 의도한 풀이 방식인 것 같다 (모범 답안 느낌)
다음에 다시 풀 때 꼭 이번 풀이를 기억하도록..
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        # 떨어진 경우
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        # 안 떨어진 경우
        stack.append(i)
            
    # 마지막까지 스택에 값이 남은 경우
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
        
    return answer

'''
# 260701 (복습)
지난 번의 풀이 중 스택을 써야한다는 건 기억하고 있었지만, 
단순히 기억나는 대로 풀기보다 스스로 논리적으로 풀이 과정을 
고려하면서 풀이했더니 여러 번 실패 끝에 성공할 수 있었다!
'''
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        price = prices[i]
        
        while stack and price < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append(i)
            
    while stack:
        idx = stack.pop()
        answer[idx] = i - idx
        
    return answer