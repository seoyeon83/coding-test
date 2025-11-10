'''

1. 자주 나올 수록 앞에
2. 단어 길이가 길 수록 앞에
3. 사전 순으로 앞에 있는 단어일 수록 앞에 

M 이상인 단어만 외운다

먼저 단어 개수를 M 이상인 것으로 
근데 중복 제거가 필요함

아래 로직은 시간 초과 문제가 있음
저장할 때 카운트를 같이 진행해보자 -> 해결
'''

import sys 

N, M = map(int ,sys.stdin.readline().split())

# 단어 길이가 M 이상인 것만 저장
words = list()
words_cnt = dict()
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= M:
        words.append(word)
        # 카운트
        if word in words_cnt.keys():
            words_cnt[word] += 1
        else:
            words_cnt[word] = 0

# 중복 제거
answer = list(set(words))

# 사전순 정렬
answer.sort()
# 빈도, 길이로 정렬
answer.sort(key=lambda x: (words_cnt[x], len(x)), reverse=True)

for a in answer:
    print(a)