def dfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited.add(start)
    print(start, end=' ')

    # 인접 노드 재귀적으로 방문
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    '1': ['2', '3', '8'],
    '2': ['1', '7'],
    '3': ['1', '4', '5'],
    '4': ['3', '5'],
    '5': ['3', '4'],
    '6': ['7'],
    '7': ['6', '8'],
    '8': ['1', '7'],
}

visited = set()

dfs(graph, '1', visited)