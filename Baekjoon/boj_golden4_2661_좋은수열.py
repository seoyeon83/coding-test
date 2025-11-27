'''
1,2,3으로만 이루어지는 수열
인접한 두 개 부분 수열이 동일한 것이 있으면 나쁜 수열
33, 32121323, 123123213

같은 패턴이 한 번이라도 반복되면 안된다

길이가 숫자 N인 수열 중 가장 작은 좋은 수열

수열 만드는 메소드를 사용해서 수열을 만든 뒤, 좋은 수열인지 아닌지 판별하기?
근데 어떻게 좋은 수열, 나쁜 수열을 판단하는가? 
N/2 길이의 모든 수열의 경우의수를 찾고, 그걸 연속으로 한 게 수열 안에 있는지 유무로 필터링?
근데 그러면 너무 메모리초과가 되지 않을까?

1, 2, 3 순서대로 붙이면서 나쁜순열인지 아닌지 체크

백트래킹 
'''

import sys 


# 나쁜 순열인지 아닌지 검사
# 추가된 부분에 대해서만 검사 
def isgood(num):
    for i in range(1, len(num)//2+1):
        if num[-i:] == num[-2*i:-i]:
            return False

    return True
        
def dfs(num):
    if len(num) == N:
        print(num)
        sys.exit()

    for c in '123':
        if isgood(num + c):
            dfs(num + c)


N = int(sys.stdin.readline())
dfs('1')