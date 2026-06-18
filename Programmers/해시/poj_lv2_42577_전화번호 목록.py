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

'''
260617
내가 왜 set 말고 dict를 썼지..?
개선:
    1) 단순 존재 여부 확인은 dict 말고 set 사용
    2) 더 단순한 풀이가 있다 (startswith() 활용) -> "119".startswith("1")    # True
'''
def solution(phone_book):
    d = {phone:True for phone in phone_book}
    m = len(min(phone_book, key=len))
    phone_book.sort()
    for phone in phone_book[1:]:
        for i in range(m, len(phone)):
            if d.get(phone[:i], False):
                return False
        
    return True
# 개선 1
def solution(phone_book):
    sets = {phone_book}
    m = len(min(phone_book, key=len))
    phone_book.sort()
    for phone in phone_book[1:]:
        for i in range(m, len(phone)):
            if phone[:i] in sets:
                return False
        
    return True
# 개선 2 - 더 단순한 풀이
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False   
    return True

'''
260618 - 복습
음.. 근데 전에 공부한 대로 전혀 안 풀었다. 
하지만 틀린 건 아니기 때문에 다음에 풀 때는 지난 풀이를 떠올려볼 수 있으면 좋겠다.
'''

def solution(phone_book):
    s = set(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in s:
                return False
            
    return True