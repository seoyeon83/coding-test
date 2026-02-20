'''
컴퓨터가 상호간 연결되어 있음
A - B - C => A, C도 간접적으로 연결됨 => A, B, C는 같은 네트워크 상에 있다

네트워크의 개수를 return?

각 컴퓨터의 개수는 n
   0  1  2
0: 1, 1, 0 => 0, 1이랑 연결
1: 1, 1, 0 => 0, 1이랑 연결
2: 0, 0, 1 => 2랑 연결 (연결 안됨)

그룹 수 2개

   0  1  2
0: 1, 1, 0 => 0, 1이랑 연결
1: 1, 1, 1 => 0, 1, 2랑 연결
2: 0, 1, 1 => 1, 2랑 연결 

그룹 수 1개

결국 이거 그룹 수 찾는 거잖아? (dfs로다가)
'''

def solution(n, computers):
    answer = 0
    visited = set()
    
    # 컴퓨터 0 ~ n-1까지 순회하면서 네트워크 그룹 수 찾기
    for i in range(n):
        if i not in visited: # dfs 수행
            visited.add(i)
            stack = [i]
            
            while stack:
                node = stack.pop()
                
                for j in range(n):
                    if computers[node][j] == 1 and j not in visited:
                        visited.add(j)
                        stack.append(j)
            answer += 1
    
    return answer