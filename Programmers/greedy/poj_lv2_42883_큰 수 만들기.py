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