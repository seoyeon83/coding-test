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

print(solution(4, [[1, 2], [1, 3], [1, 4]]))