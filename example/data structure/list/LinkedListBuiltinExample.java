import java.util.LinkedList;

public class LinkedListBuiltinExample {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();

        // 맨 앞에 요소 추가
        list.addFirst(10);
        list.addFirst(20);

        // 맨 뒤에 요소 추가
        list.addLast(30);

        // [20, 10, 30]
        System.out.println("전체 리스트: " + list);

        // 첫 요소 삭제
        list.removeFirst(); // 20 삭제

        System.out.println("첫 요소 삭제 후: " + list);
    }
}