class Node:
    """이진 트리의 기본 단위인 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 노드가 저장하는 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None # 트리의 시작점(루트)

    # -------------------- 추가 (Insertion) --------------------
    def insert(self, data):
        """데이터를 트리에 추가합니다."""
        # 트리가 비어있으면 새 노드를 루트로 설정
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        """재귀를 이용한 노드 추가 헬퍼 함수"""
        if data < current_node.data:
            # 삽입할 데이터가 더 작으면 왼쪽으로 이동
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data > current_node.data:
            # 삽입할 데이터가 더 크면 오른쪽으로 이동
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)
        # 데이터가 이미 존재하면 아무것도 하지 않음

    # -------------------- 순회 (Traversal) --------------------
    
    # 1. 전위 순회 (Pre-order: Root -> Left -> Right)
    def print_preorder(self):
        print("전위 순회 (Pre-order): ", end="")
        self._preorder_recursive(self.root)
        print()

    def _preorder_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    # 2. 중위 순회 (In-order: Left -> Root -> Right)
    # (이진 탐색 트리에서 중위 순회는 오름차순 정렬된 결과를 출력합니다)
    def print_inorder(self):
        print("중위 순회 (In-order):  ", end="")
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    # 3. 후위 순회 (Post-order: Left -> Right -> Root)
    def print_postorder(self):
        print("후위 순회 (Post-order): ", end="")
        self._postorder_recursive(self.root)
        print()

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")
            
    # -------------------- 삭제 (Deletion) --------------------
    def delete(self, data):
        """데이터를 트리에서 삭제합니다."""
        self.root = self._delete_recursive(self.root, data)

    def _find_min_value_node(self, node):
        """특정 서브트리에서 가장 작은 값을 가진 노드를 찾는 함수"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, current_node, data):
        if current_node is None:
            return None # 삭제할 데이터가 트리에 없음

        # 삭제할 데이터를 찾아 재귀적으로 내려감
        if data < current_node.data:
            current_node.left = self._delete_recursive(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(current_node.right, data)
        else:
            # 삭제할 노드를 찾았을 경우!

            # Case 1 & 2: 자식이 없거나 하나만 있는 경우
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Case 3: 자식이 둘 다 있는 경우
            # 오른쪽 서브트리에서 가장 작은 노드(in-order successor)를 찾음
            min_val_node = self._find_min_value_node(current_node.right)
            # 현재 노드의 데이터를 successor의 데이터로 교체
            current_node.data = min_val_node.data
            # 원래 successor가 있던 자리의 노드를 삭제
            current_node.right = self._delete_recursive(current_node.right, min_val_node.data)
            
        return current_node

# --- 메인 실행 블록 ---
if __name__ == "__main__":
    bst = BinarySearchTree()

    # 1. 노드 추가
    print("--- 1. 노드 추가 ---")
    nodes_to_insert = [50, 30, 20, 40, 70, 60, 80]
    for node_data in nodes_to_insert:
        bst.insert(node_data)
        print(f"'{node_data}' 삽입 완료.")

    # 2. 초기 순회 결과 출력
    print("\n--- 2. 초기 순회 결과 ---")
    bst.print_preorder()
    bst.print_inorder()
    bst.print_postorder()

    # 3. 노드 삭제
    print("\n--- 3. 노드 삭제 ---")
    
    # Case 1: 자식이 없는 노드(20) 삭제
    print("\n삭제할 노드: 20 (자식 없음)")
    bst.delete(20)
    bst.print_inorder()
    
    # Case 2: 자식이 하나인 노드(30) 삭제
    print("\n삭제할 노드: 30 (자식 하나)")
    bst.delete(30)
    bst.print_inorder()
    
    # Case 3: 자식이 둘인 노드(50, 루트) 삭제
    print("\n삭제할 노드: 50 (자식 둘)")
    bst.delete(50)
    bst.print_inorder()

    # 4. 최종 순회 결과 출력
    print("\n--- 4. 최종 순회 결과 ---")
    bst.print_preorder()
    bst.print_inorder()
    bst.print_postorder()