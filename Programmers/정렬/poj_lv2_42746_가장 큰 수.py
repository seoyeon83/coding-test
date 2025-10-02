from functools import cmp_to_key

def cmp(a, b):
    if a+b > b+a:
        return -1   # a가 앞에 와야 함
    if a+b < b+a:
        return 1    # b가 앞에 와야 함
    return 0        # 같음
    
def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=cmp_to_key(cmp))
    
    answer = ''.join(numbers_str)
    
    return '0' if answer[0] == '0' else answer