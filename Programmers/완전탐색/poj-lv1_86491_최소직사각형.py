'''
다양한 모양과 크기의 명함들을 모두 수납 가능하면서 작아서 들고 다니기 편한 지갑
모든 명함의 가로, 세로 길이 조사
명함을 90도 회전해 수납할 수 있음
그러면 입력받은 가로, 세로 길이를 더 큰 숫자가 앞에 오게 처리
이 경우 가장 긴 가로 길이와 가장 긴 세로 길이를 찾아 곱함 
'''

### 1번째 풀이
def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[1], size[0] = size[0], size[1]
    
    w, h = [], []
    for a, b in sizes:
        w.append(a)
        h.append(b)
        
    return max(w) * max(h)

### 2번째 풀이
def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[1], size[0] = size[0], size[1]
    
    return max(sizes, key=lambda x: x[0])[0] * max(sizes, key=lambda x: x[1])[1] 