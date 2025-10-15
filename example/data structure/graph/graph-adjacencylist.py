# 딕셔너리를 사용한 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 간선 추가 (무방향)
def add_edge(graph, u, v):
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# 간선 삭제 (무방향)
def remove_edge(graph, u, v):
    try:
        graph[u].remove(v)
        graph[v].remove(u)
    except (KeyError, ValueError):
        print(f"\n간선 ({u}, {v})를 찾을 수 없습니다.")

# 정점 및 간선 관련 모두 삭제
def remove_vertex(graph, vertex):
    if vertex not in graph:
        print(f"\n삭제할 정점 '{vertex}'가 그래프에 없습니다.")
        return

    # 1. 정점과 연결된 다른 모든 노드들의 인접 리스트에서 이 정점을 제거
    for neighbor in list(graph[vertex]): # list()로 복사 후 순회
        graph[neighbor].remove(vertex)

    # 2. 딕셔너리에서 해당 정점의 항목(key)을 완전히 삭제
    del graph[vertex]

# 그래프 출력
def print_graph(graph):
    for vertex, neighbors in graph.items():
        print(f"정점 {vertex} -> {neighbors}")


# 새로운 그래프 생성
my_graph = {}
print("--- 1. 그래프 구성 ---")
add_edge(my_graph, 0, 1)
add_edge(my_graph, 0, 2)
add_edge(my_graph, 1, 2)
add_edge(my_graph, 2, 3)

print_graph(my_graph, "초기 그래프 상태")

# 간선 (1, 2) 삭제
remove_edge(my_graph, 1, 2)
print_graph(my_graph, "간선 (1, 2) 삭제 후")

# 정점 2 삭제
remove_vertex(my_graph, 2)
print_graph(my_graph, "정점 2 삭제 후")