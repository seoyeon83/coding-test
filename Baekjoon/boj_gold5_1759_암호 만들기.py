'''
최소 한 개의 모음 aeiou, 최소 두 개의 자음으로 구성됨
정렬된 것 -> 일단 정렬한 상태로 저장

길이는 L이어야 하고
C개의 알파벳 중에서 조합을 해야한다

그러면 자음이 1개 들어간 경우, 2개 들어간 경우, 3개,..? 

백트래킹으로 하고 조합이 맞는지 안 맞는지 체크하는 함수를 만들고?
'''

import sys 


# 조건에 맞는지 체크
j = ['a', 'e', 'i', 'o', 'u']
def check(string):
    cnt = 0
    for c in string:
        if c in j:
            cnt += 1

    if cnt >= 1 and len(string)-cnt >= 2:
        return True
    
    return False


def dfs(string, i):
    if len(string) == L and check(string):
        print(string)
        return

    for c in a[i:]:
        if c not in string and string[-1] < c:
            new_string = string + c 
            dfs(new_string, i+1)


L, C = map(int, sys.stdin.readline().split())
a = sorted(sys.stdin.readline().split())

for n in range(C-L+1):
    dfs(a[n], n)