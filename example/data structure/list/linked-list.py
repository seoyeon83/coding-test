# 노드(데이터 저장 단위) 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    # 리스트 맨 앞에 데이터 추가
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 데이터로 노드 삭제
    def delete_node(self, key):
        current = self.head

        # 1. 삭제할 노드가 헤드(head)인 경우
        if current is not None and current.data == key:
            self.head = current.next
            current = None # 메모리에서 연결 끊기
            print(f"데이터 '{key}'를 가진 헤드 노드를 삭제했습니다.")
            return

        # 2. 헤드가 아닌 다른 노드를 삭제하는 경우
        prev = None
        # key를 가진 노드를 찾을 때까지 순회
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # key를 가진 노드가 리스트에 없는 경우
        if current is None:
            print(f"데이터 '{key}'가 리스트에 존재하지 않습니다.")
            return

        # 찾았다면, 이전 노드(prev)의 next를 현재 노드(current)의 next로 연결
        prev.next = current.next
        current = None # 메모리에서 연결 끊기
        print(f"데이터 '{key}'를 가진 노드를 삭제했습니다.")


    # 리스트 출력
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- 사용 예제 ---
my_list = LinkedList()
my_list.insert_at_beginning(50)
my_list.insert_at_beginning(40)
my_list.insert_at_beginning(30)
my_list.insert_at_beginning(20)
my_list.insert_at_beginning(10)

print("원본 리스트:")
my_list.print_list()

# 중간 노드(30) 삭제
my_list.delete_node(30)
my_list.print_list()

# 헤드 노드(10) 삭제
my_list.delete_node(10)
my_list.print_list()

# 없는 값 삭제 시도
my_list.delete_node(99)
my_list.print_list()