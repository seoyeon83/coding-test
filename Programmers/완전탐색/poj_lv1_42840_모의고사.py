# 1) 1 2 3 4 5 ...
# 2) 2 1 2 3 2 4 2 5 ...
# 4) 3 3 1 1 2 2 4 4 5 5 ...

def solution(answers):
    s1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    cnt = [0, 0, 0]
    for a, f, s, t in zip(answers, s1, s2, s3):
        if a == f:
            cnt[0] += 1
        if a == s:
            cnt[1] += 1
        if a == t:
            cnt[2] += 1

    # 가장 많이 맞힌 사람 찾기
    return [i+1 for i, n in enumerate(cnt) if n == max(cnt)]


### 251010 다시 푼 버전 (로직이 똑같네)

'''
1: 1,2,3,4,5 ...
2: 2,1,2,3,2,4,2,5, ...
3: 3,3,1,1,2,2,4,4,5,5,...

1. 문제 길이에 맞춰서 수포자별 답지 세팅
2. 수포자별 몇 문제 맞췄는지 카운드
3. 최대값만큼 맞춘 사람들은 answer에 넣어서 리턴
'''

def solution(answers):
    n = len(answers)
    a = [1,2,3,4,5] * (n//5+1)
    b = [2,1,2,3,2,4,2,5] * (n//8+1)
    c = [3,3,1,1,2,2,4,4,5,5] * (n//10+1)
    
    cnt = [0, 0, 0]
    for i in range(n):
        if answers[i] == a[i]: cnt[0] += 1
        if answers[i] == b[i]: cnt[1] += 1
        if answers[i] == c[i]: cnt[2] += 1
    
    answer = [i+1 for i in range(3) if cnt[i] == max(cnt)]
    
    return answer