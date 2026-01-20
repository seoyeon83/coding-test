'''
전형적인 스택 문제인듯
올바른 괄호인지 아닌지 확인한다 
열려있는 ( 괄호라면 push, 닫혀있는 괄호라면 pop해서 pop한 값이 열린 괄호면 통과
스택에 괄호가 남아있으면 false
'''

# def solution(s):
#     stack = []
    
#     for c in s:
#         if c == "(":
#             stack.append(c)
#         elif stack: # 닫힌 괄호이고 stack에 값이 있는 경우 
#             stack.pop()
#         else: # 닫힌 괄호이고 stack에 값이 없는 경우 -> false
#             return False
        
#     if stack: return False
#     return True


'''
260120 다시 풀었음

s 길이가 홀수 개면 False (짝이 안 맞으니까)

( => push
) => pop

s를 다 순회하고도 stack에 값이 남아있으면 False, 없으면 True

첫 번째로 풀었을 때보다 깔끔한 것 같다!

세 번재 조건 (not(stack) and c == ') 은 '()))' 과 같은 경우를 위한 것
없어도 프로그래머스의 케이스에는 없어서 통과가 되긴 함
'''

def solution(s):
    if len(s) % 2 == 1: 
        return False

    stack = list()
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack and c == ')':
            stack.pop()
        else: # not(stack) and c == ')
            return False
    
    if stack:
        return False
    return True

print(solution('()))'))