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