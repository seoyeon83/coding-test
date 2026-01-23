# 처음 짠 코드 (효율성 테스트 통과 못함)
def solution(phone_book):
    # 길이로 정렬
    phone_book.sort(key=lambda x: len(x))
    
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if phone_book[i] == j[:len(phone_book[i])]:
                return False
            
    return True

# gemini 힌트를 보고 짠 코드 (접두어 활용)
def solution(phone_book):
    d = { x : True for x in phone_book }
    
    for x in phone_book:
        for i in range(len(x)-1):
            if x[:i+1] in d.keys():
                return False
    
    return True


'''
260123에 다시 푼 것
'''
def solution(phone_book):
    d = set(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in d:
                return False
    return True