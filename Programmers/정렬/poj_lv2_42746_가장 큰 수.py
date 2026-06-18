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


'''
260208
줄여보기..
'''
def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), reverse=True, key=lambda x: x*3))))

'''
260618
접근: 반복 정렬
    기본 문자열 정렬이 아니라 반복 정렬을 진행한다
    3과 30을 비교할 때 3이 앞으로 와야 최댓값을 만들 수 있다 (3+30 => 330)
    하지만 기본 문자열 정렬 시, 30 + 3 순서가 된다
    이때 문자열을 3번 반복시켜 비교한다. 333 vs 303030 => 두 번째 자리에서 3>0이 되어서 3이 앞으로 올 수 있다
    3번 반복시키는 이유는 한 자릿수와 최대 세 자릿수를 비교해야 하기 때문. (원소는 최대 1000. 1000은 1로 시작해서 웬만하면 정렬에서 밀려나므로 3자리로 맞춘다)
*다음에 다시 풀어볼 때는 [0, 0, 0]처럼 배열의 값이 모두 0인 경우도 잘 고려할 수 있도록 할 것 (cmp 활용)

'''
def solution(numbers):
    answer = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return "0" if answer[0] == "0" else ''.join(answer)