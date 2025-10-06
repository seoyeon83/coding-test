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