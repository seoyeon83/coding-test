def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        # 방문
        node = stack.pop()
        if node not in visited:
            # 방문 처리
            visited.add(node)
            print(node, end=' ')
            # 인접 노드 스택에 미방문 노드 추가
            # 후입선출이므로 역순으로 넣어야 함
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# 예시 그래프 (무방향 그래프)
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

# DFS 수행
dfs(graph, '1')