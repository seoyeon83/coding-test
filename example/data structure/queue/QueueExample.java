import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        // 요소 추가 (add 또는 offer)
        queue.add("고객1");
        queue.add("고객2");
        queue.add("고객3");

        System.out.println("현재 대기열: " + queue);

        // 맨 앞 요소 확인 (peek)
        System.out.println("다음 고객: " + queue.peek()); // 고객1

        // 요소 꺼내기 (remove 또는 poll)
        String served = queue.remove();
        System.out.println("서비스 받은 고객: " + served); // 고객1
        System.out.println("서비스 후 대기열: " + queue);
    }
}