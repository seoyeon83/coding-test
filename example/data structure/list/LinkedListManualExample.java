public class LinkedListManualExample {

    // 노드 클래스
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    Node head; // 리스트의 시작점

    // 리스트 맨 앞에 노드 추가
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    // 리스트 출력
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        LinkedListManualExample myList = new LinkedListManualExample();
        myList.insertAtBeginning(30);
        myList.insertAtBeginning(20);
        myList.insertAtBeginning(10);

        myList.printList();
    }
}