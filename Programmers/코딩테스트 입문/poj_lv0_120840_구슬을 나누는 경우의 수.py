'''
갖고 있는 구슬의 개수 balls
친구들에게 나누어 줄 구슬 개수 share
balls 개의 구슬 중 share 개의 구슬을 고르는 가능한 모든 경우의 수
순서 고려 X
balls C share
'''
def factorial(n): 
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))
    