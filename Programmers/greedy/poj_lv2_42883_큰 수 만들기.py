def solution(number, k):
    numbers = [int(c) for c in number]
    stack = numbers[:1]
    
    for n in numbers[1:]:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1

        if len(stack) < len(numbers) - k:
            stack.append(n)
        
    return ''.join(map(str, stack))


print(solution("333222111", 3))
print(solution("10", 1))

'''
# 260626
생각한 접근은 좀 맞는 것 같은데 문제는 정확히 어떻게 구현해야 할지 잘 모르겠더라...
지난 나의 풀이를 참고해 공부했으므로 별도 코드는 올리지 않겠다

# 260702 
흠.. 재시도했는데 이전에 이해를 잘 못했는지 제대로 못 풀었다 (스택을 잘 못쓰는 듯..)
밑 코드는 공부용으로 기록한다

'''

def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()      # 앞의 작은 걸 버림
            k -= 1
        stack.append(n)
    if k > 0:                # 다 훑었는데 지울 게 남으면(내림차순이었던 경우)
        stack = stack[:-k]   # 뒤에서 k개 자름
    return ''.join(stack)

'''
# 260703
어제 풀이를 기반으로 혼자 풀어보려고 했다. 조오금 다르긴 하지만 가장 중요한 로직은 그대로 스스로 떠올리고 재현해냈다! 
'''
def solution(number, k):
    stack = [number[0]]
    
    for n in number[1:]:
        while stack and k > 0 and n > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(n)

    # 내림차순이나 다 같은 숫자인 경우를 위해 뒤에서부터 지우기
    while stack and k > 0:
        stack.pop()
        k -= 1
        
    return ''.join(stack)