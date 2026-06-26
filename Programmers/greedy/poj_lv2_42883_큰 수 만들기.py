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
'''