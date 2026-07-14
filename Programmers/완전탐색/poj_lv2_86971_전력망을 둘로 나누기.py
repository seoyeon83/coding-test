def dfs(graph, j):
    cnt, visited = 0, set()
    stack = [j]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            for j in reversed(graph[n]):
                if j not in visited:
                    stack.append(j)
    
    return visited
    
def wires_to_graph(n, wires):
    graph = {i:list() for i in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)): 
        # 인덱스 i 제외 후 graph 만들기
        graph = wires_to_graph(n, wires[:i] + wires[i+1:])
        groups, visited = list(), set()
        
        for j in range(1, n+1):
            # 그룹이 세 개 이상이면 break
            if len(groups) > 2: break

            # 그룹이 또 존재하고 노드가 두 개 이상인 경우
            if graph[j] and j not in visited:
                v = dfs(graph, j)
                groups.append(len(v))
                visited.update(v)
            
            # 그룹이 또 존재하는데 노드가 하나 뿐인 경우
            if j not in visited:
                groups.append(1)

        # 결과 업데이트
        if len(groups) == 2:
            result = abs(groups[0] - groups[1])
            answer = result if result < answer else answer
    
    return answer

'''
# 260714
접근: combinations로 전선 한 개를 뺀 조합을 만들고, 그걸 기반으로 인접 양방향 그래프를 딕셔너리로 표현
    그래프를 탐색하면서 나눠진 두 영역의 노드 개수를 세서 비교한다
개선점: 
    1) 기존에는 두 영역을 다 셌는데 사실 한 영역만 세면 된다
    2) dfs(, , visited=set()) 으로 설정하고 만약 이 설정으로 set()이 호출되면 이 함수 안에서는 visited를 모든 호출이 공유한다
    3) cnt로 따로 세지 않아도 visited 개수를 세면 된다
    4) 좀 더 의미를 살려서 함수명/변수명 개선
'''

from itertools import combinations 


def dfs(graph, start, visited=set()):
    stack = [start]
    cnt = 0
    
    while stack:
        n = stack.pop()
        if n not in visited:
            cnt += 1
            visited.add(n)
            for i in graph[n]:
                stack.append(i)
    
    return cnt, visited


def solution(n, wires):
    answer = n
    for comb in combinations(wires, len(wires)-1):
        graph = {i:[] for i in range(1, n+1)}
        visited = set()
        result = []
        for a, b in comb:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, n+1):
            if i not in visited:
                r, visited = dfs(graph, i, visited)
                result.append(r)
            
        answer = min(answer, abs(result[0]-result[1]))

    return answer

# 개선

from itertools import combinations 


def count_nodes(graph, start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    return len(visited)


def solution(n, wires):
    answer = n
    for kept in combinations(wires, len(wires)-1):
        graph = {i:[] for i in range(1, n+1)}
        for a, b in kept:
            graph[a].append(b)
            graph[b].append(a)
        
        size = count_nodes(graph, 1)
            
        answer = min(answer, abs(2 * size - n))

    return answer