'''
n을 기준으로 n과 가까운 수부터 정렬하자
모두 정수
거리가 같은 경우 더 큰 숫자(먼저 정렬)
'''

def solution(numlist, n):
    numlist.sort(reverse=True)
    return sorted(numlist, key=lambda x: abs(x-n))