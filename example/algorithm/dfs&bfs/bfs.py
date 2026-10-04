from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            # 방문
            visited.add(node)
            print(node, end=' ')
            # 인접 노드 중 미방문 노드 push 후 순서대로 방문
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

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

# BFS 수행
bfs(graph, '1')


# 이코테 버전
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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
bfs(graph, 1, visited)