# 정점의 개수
vertices = 4
# 0으로 초기화된 2차원 리스트 생성
adj_matrix = [[0] * vertices for _ in range(vertices)]

# 간선 추가 함수 (무방향)
def add_edge_matrix(matrix, u, v):
    matrix[u][v] = 1
    matrix[v][u] = 1

# 간선 삭제 (무방향)
def remove_edge_matrix(matrix, u, v):
    matrix[u][v] = 0
    matrix[v][u] = 0
    

print("--- 1. 그래프 구성 ---")
# 간선 추가
add_edge_matrix(adj_matrix, 0, 1)
add_edge_matrix(adj_matrix, 0, 2)
add_edge_matrix(adj_matrix, 1, 2)
add_edge_matrix(adj_matrix, 2, 3)

# 초기 인접 행렬 출력
print("\n초기 인접 행렬:")
for row in adj_matrix:
    print(row)

# 간선 삭제 실행
remove_edge_matrix(adj_matrix, 1, 2)

# 삭제 후 인접 행렬 출력
print("\n간선 삭제 후 인접 행렬:")
for row in adj_matrix:
    print(row)