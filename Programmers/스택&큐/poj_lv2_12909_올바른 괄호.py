'''
전형적인 스택 문제인듯
올바른 괄호인지 아닌지 확인한다 
열려있는 ( 괄호라면 push, 닫혀있는 괄호라면 pop해서 pop한 값이 열린 괄호면 통과
스택에 괄호가 남아있으면 false
'''

def solution(s):
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif stack: # 닫힌 괄호이고 stack에 값이 있는 경우 
            stack.pop()
        else: # 닫힌 괄호이고 stack에 값이 없는 경우 -> false
            return False
        
    if stack: return False
    return True