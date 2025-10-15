public class BinaryTreeExample {

    // 트리의 기본 단위인 노드 클래스 (내부 클래스로 정의)
    static class Node {
        int data;
        Node left;
        Node right;

        // 생성자
        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    // 이진 트리의 시작점(루트)
    Node root;

    public BinaryTreeExample() {
        root = null;
    }

    // -------------------- 추가 (Insertion) --------------------
    public void insert(int data) {
        root = insertRec(root, data);
    }

    // 재귀를 이용한 노드 추가 헬퍼 함수
    private Node insertRec(Node current, int data) {
        // 현재 노드가 null이면, 새로운 노드를 생성하여 반환
        if (current == null) {
            return new Node(data);
        }

        // 삽입할 데이터가 현재 노드보다 작으면 왼쪽으로 이동
        if (data < current.data) {
            current.left = insertRec(current.left, data);
        }
        // 삽입할 데이터가 현재 노드보다 크면 오른쪽으로 이동
        else if (data > current.data) {
            current.right = insertRec(current.right, data);
        }
        // (데이터가 이미 존재하면 아무것도 하지 않음)

        return current;
    }

    // -------------------- 순회 (Traversal) --------------------
    
    // 1. 전위 순회 (Pre-order: Root -> Left -> Right)
    public void printPreorder() {
        System.out.print("전위 순회 (Pre-order): ");
        preorderRec(root);
        System.out.println();
    }

    private void preorderRec(Node node) {
        if (node != null) {
            System.out.print(node.data + " ");
            preorderRec(node.left);
            preorderRec(node.right);
        }
    }

    // 2. 중위 순회 (In-order: Left -> Root -> Right)
    // 이진 탐색 트리에서 중위 순회는 오름차순으로 정렬된 결과를 출력합니다.
    public void printInorder() {
        System.out.print("중위 순회 (In-order):  ");
        inorderRec(root);
        System.out.println();
    }

    private void inorderRec(Node node) {
        if (node != null) {
            inorderRec(node.left);
            System.out.print(node.data + " ");
            inorderRec(node.right);
        }
    }
    
    // 3. 후위 순회 (Post-order: Left -> Right -> Root)
    public void printPostorder() {
        System.out.print("후위 순회 (Post-order): ");
        postorderRec(root);
        System.out.println();
    }

    private void postorderRec(Node node) {
        if (node != null) {
            postorderRec(node.left);
            postorderRec(node.right);
            System.out.print(node.data + " ");
        }
    }
    
    // -------------------- 삭제 (Deletion) --------------------
    public void delete(int data) {
        root = deleteRec(root, data);
    }

    // 재귀를 이용한 노드 삭제 헬퍼 함수
    private Node deleteRec(Node current, int data) {
        if (current == null) {
            return null;
        }

        // 삭제할 노드를 찾아 내려감
        if (data < current.data) {
            current.left = deleteRec(current.left, data);
        } else if (data > current.data) {
            current.right = deleteRec(current.right, data);
        } else {
            // 삭제할 노드를 찾았을 경우!
            
            // Case 1: 자식 노드가 없는 경우 (리프 노드)
            // Case 2: 자식 노드가 하나만 있는 경우
            if (current.left == null) {
                return current.right;
            } else if (current.right == null) {
                return current.left;
            }
            
            // Case 3: 자식 노드가 둘 다 있는 경우
            // 오른쪽 서브트리에서 가장 작은 값을 찾아서 현재 노드의 값으로 대체
            current.data = findMinValue(current.right);
            // 대체된 노드(가장 작은 값)를 오른쪽 서브트리에서 삭제
            current.right = deleteRec(current.right, current.data);
        }
        return current;
    }

    // 특정 서브트리에서 가장 작은 값을 찾는 함수
    private int findMinValue(Node node) {
        int minValue = node.data;
        while (node.left != null) {
            minValue = node.left.data;
            node = node.left;
        }
        return minValue;
    }


    // -------------------- 메인 함수 (실행 예제) --------------------
    public static void main(String[] args) {
        BinaryTreeExample tree = new BinaryTreeExample();

        // 1. 노드 추가
        System.out.println("--- 1. 노드 추가 ---");
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // 2. 초기 순회 결과 출력
        System.out.println("\n--- 2. 초기 순회 결과 ---");
        tree.printPreorder();
        tree.printInorder();
        tree.printPostorder();

        // 3. 노드 삭제
        System.out.println("\n--- 3. 노드 삭제 ---");
        
        // Case 1: 자식이 없는 노드(20) 삭제
        System.out.println("\n삭제할 노드: 20 (자식 없음)");
        tree.delete(20);
        tree.printInorder();
        
        // Case 2: 자식이 하나인 노드(30) 삭제
        System.out.println("\n삭제할 노드: 30 (자식 하나)");
        tree.delete(30);
        tree.printInorder();
        
        // Case 3: 자식이 둘인 노드(50, 루트) 삭제
        System.out.println("\n삭제할 노드: 50 (자식 둘)");
        tree.delete(50);
        tree.printInorder();

        // 4. 최종 순회 결과 출력
        System.out.println("\n--- 4. 최종 순회 결과 ---");
        tree.printPreorder();
        tree.printInorder();
        tree.printPostorder();
    }
}