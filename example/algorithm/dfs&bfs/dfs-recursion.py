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


# 이코테 버전 (dict 대신 list 사용, visited도 bool 값이 담긴 list 사용)
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)