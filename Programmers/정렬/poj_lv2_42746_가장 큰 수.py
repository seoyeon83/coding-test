'''
# 정수를 이어 붙여 만들 수 있는 가장 큰 수
# 배열의 값을 모두 문자열로 만들고 내림차순 정렬하여 붙이면?

아 근데 대부분 괜찮은데 아래의 경우가 문제	
[3, 30, 34, 5, 9] -> 실행한 결괏값 "9534303"이 기댓값 "9534330"과 다릅니다.

그러면 당장 비교하는 수가 같은데 한 수는 남은 자릿수가 없고, 다른 것은 나머지 자릿수가 있는 경우 세 가지 경우로 나뉨 
3, 30 -> 330 (한 자릿수가 먼저) 
3, 33 -> 333 (상관없음)
3, 35 -> 353 (두 자릿수가 먼저)

cmp_to_key를 활용해서 성공
'''
from functools import cmp_to_key

def func(a, b):
    if a+b > b+a:
        return -1
    if a+b < b+a:
        return 1
    
    return 0 
    
def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=cmp_to_key(func))
    
    answer = ''.join(numbers_str)
    
    return '0' if answer[0] == '0' else answer