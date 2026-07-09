def solution(brown, yellow):
    
    n = brown+yellow # 넓이
    h = 3 # 최소 높이
    while True:
        w = n//h
        # 넓이가 h로 나누어 떨어지는지, 제대로 그 카펫이 맞는지 확인 
        if n%h==0 and (w+h-2)*2==brown:
            return [w, h]
        h += 1

print(solution(10, 2))


'''
260214
'''
def solution(brown, yellow):
    s = brown + yellow
    for a in range(2, int(s/2) + 1):
        if s%a == 0 :
            b = s // a
            if (a + b) * 2 - 4 == brown and (a - 2) * (b - 2) == yellow:
                return [b, a]
            

'''
# 260709
접근: brown과 yellow를 기반으로 w, h를 변수로 하는 방정식 두 개를 만들어서 그 방정식을 충족하는 w, h 값을 찾는다 
    (사실 이차방정식이라 바로 답을 구할 수도 있긴 한데 그냥 직관적으로 for문으로 탐색하는 방식으로 찾다)
    brown = 2 * w + 2 * (h - 2) = 2*w + 2h - 4
    yellow = (w-2) * (h-2) = w*h - 2*w - 2*h + 4 
    yellow가 1 이상이므로 h는 최소 3이다 (중앙에 yellow, 테두리에 brown이 한개씩 있으므로)
    이걸 기반으로 for문 범위를 3 ~ (brown + yellow)//3 으로 정의한다. 이때 w, h가 맞아떨어지는지 확인하고 방정식을 기반으로 답인지 판단한다

개선점: yellow 거사는 불필요하다는 것.. brown == 2*w+2*h-4 이게 맞으면 yellow도 자동으로 참이 되므로 brown, yellow 둘 중 하나만 해도 된다

이게 맞나 하면서 풀었는데 이전 풀이와 비슷해서 놀랐다. 그동안 푼 것 중 가장 마음에 드는 풀이.
'''
def solution(brown, yellow):
    area = brown + yellow
    
    for h in range(3, area//3+1):
        if area % h == 0:
            w = area//h
            if (brown == 2*w+2*h-4) and (yellow == w*h - 2*w - 2*h + 4):
                return [w, h]