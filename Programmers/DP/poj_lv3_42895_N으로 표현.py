def solution(N, number):
    answer = 0
    sets = [set() for _ in range(9)]
    for k in range(1, 9):        
        sets[k].add(int(str(N)*k))
        
        for i in range(1, k):
            for a in sets[i]:
                for b in sets[k-i]:
                    sets[k].add(a + b)
                    sets[k].add(a - b)
                    sets[k].add(a * b)
                    if b != 0:
                        sets[k].add(a // b)
                        
        if number in sets[k]:
            return k
        
    return -1
    