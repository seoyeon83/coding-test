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



# 다른 사람 풀이 참고해서 푼 것
'''
cmp 안 쓰고도 가능하네
같은 수를 곱해서 ?
3, 30, 34 는 34, 3, 30 으로 정렬되어야 이상적
이 경우는 값을 *3해서 비교?
'''

def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers_str)))